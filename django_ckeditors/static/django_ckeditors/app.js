import ClassicEditor from './src/ckeditor';
import './src/override-django.css';

let editors = [];
// Store image URLs for each editor, placeholder for future useage.
const editorImageUrls = new Map(); 

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function createEditors(element = document.body) {

    // Find all elements within the specified container (or entire document body)
    // that have the class 'django_ckeditors' (these are our CKEditor targets).
    const allEditors = resolveElementArray(element, '.django_ckeditors');

    allEditors.forEach(editorEl => {
        // Check if this element is part of a Django formset template or 
        // has already been processed.
        if (
            editorEl.id.indexOf('__prefix__') !== -1 ||
                editorEl.getAttribute('data-processed') === '1'
        ) {
            return
        }
        const script_id = `${editorEl.id}_script`;
        editorEl.nextSibling.remove();

        const upload_image_url = element.querySelector(
            `#${script_id}-ck-editors-upload-url`
        ).getAttribute('data-upload-image-url');

        const csrf_cookie_name = element.querySelector(
            `#${script_id}-ck-editors-upload-url`
        ).getAttribute('data-csrf_cookie_name');

        const data_extra = JSON.stringify(JSON.parse(element.querySelector(
            `#${script_id}-ck-editors-upload-url`
        ).getAttribute('data-extra')));

        const labelElement = element.querySelector(`[for$="${editorEl.id}"]`);
        if (labelElement) {
            labelElement.style.float = 'none';
        }
        //console.log('EXTRA DATA', data_extra)

        const config = JSON.parse(
            element.querySelector(`#${script_id}-span`).textContent,
            (key, value) => {
                var match = value.toString().match(new RegExp('^/(.*?)/([gimy]*)$'));
                if (match) {
                    var regex = new RegExp(match[1], match[2]);
                    return regex;
                }
                return value;
            }
        );
        config.simpleUpload = {
            'uploadUrl': upload_image_url, 
            'headers': {
                'X-CSRFToken': getCookie(csrf_cookie_name),
                'X-Data-Extra': data_extra,
            }
        };


        ClassicEditor.create(editorEl, config)
            .then(editor => {
                //  WordCount plugin handling
                if (editor.plugins.has('WordCount')) {
                    const wordCountPlugin = editor.plugins.get('WordCount');
                    const wordCountWrapper = element.querySelector(`#${script_id}-word-count`);
                    wordCountWrapper.innerHTML = '';
                    wordCountWrapper.appendChild(wordCountPlugin.wordCountContainer);
                };
                // Extract initial image URLs for this editor
                const previousImageUrls = extractImageUrls(editor.getData());
                editorImageUrls.set(editor, previousImageUrls);

                // Listen for content changes
                editor.model.document.on('change:data', () => {
                    const currentContent = editor.getData();
                    const currentImageUrls = extractImageUrls(currentContent);

                    // Compare and identify removed images
                    const removedImages = findRemovedImages(previousImageUrls, currentImageUrls);
                    removedImages.forEach(imageUrl => {
                        console.log('Image removed from', editor, ':', imageUrl);
                        //sendRemovedImageToServer(imageUrl, upload_unused_image_url); // Pass the URL
                    });

                    // Update the stored URLs for the next comparison
                    editorImageUrls.set(editor, currentImageUrls); 
                });

                editors.push(editor);
            })
            .catch(error => {
                console.error(error);
            });

        editorEl.setAttribute('data-processed', '1');
    });

    window.editors = editors; 
    window.ClassicEditor = ClassicEditor;
}

/**
 * Checks whether the element or its children match the query and returns
 * an array with the matches.
 * 
 * @param {!HTMLElement} element
 * @param {!string} query
 * 
 * @returns {array.<HTMLElement>}
 */
function resolveElementArray(element, query) {
    return element.matches(query) ? [element] : [...element.querySelectorAll(query)];
}


// Function to extract image URLs from CKEditor content (HTML string)
function extractImageUrls(content) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(content, 'text/html');
    const images = doc.querySelectorAll('img');

    return Array.from(images).map(img => img.src);
}

// Function to find removed image URLs by comparing two arrays
function findRemovedImages(oldImageUrls, newImageUrls) {
    return oldImageUrls.filter(imageUrl => !newImageUrls.includes(imageUrl));
}

// Function to send removed image URLs to the server
function sendRemovedImageToServer(imageUrl, endpointUrl) {
    fetch(endpointUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', 
            'X-CSRFToken': getCookie(csrf_cookie_name),
        },
        body: JSON.stringify({ imageUrl }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Or handle the response as needed by your server
        })
        .then(data => {
            console.log('Server response:', data);
        })
        .catch(error => {
            console.error('Error sending image URL:', error);
        });
}

/**
 * This function filters the list of mutations only by added elements, thus
 * eliminates the occurrence of text nodes and tags where it does not make sense
 * to try to use with `QuerySelectorAll()` and `matches()` functions.
 * 
 * @param {MutationRecord} recordList - It is the object inside the array
 * passed to the callback of a MutationObserver.
 * 
 * @returns {Array} Array containing filtered nodes.
 */
function getAddedNodes(recordList) {
    return recordList
        .flatMap(({ addedNodes }) => Array.from(addedNodes))
        .filter(node => node.nodeType === 1);
}

window.createEditors = createEditors;

document.addEventListener("DOMContentLoaded", () => {
    createEditors();

    if (typeof django === "object" && django.jQuery) {
        django.jQuery(document).on("formset:added", createEditors);
    }

    const observer = new MutationObserver((mutations) => {
        let addedNodes = getAddedNodes(mutations);

        addedNodes.forEach(node => {
            // Initializes editors
            createEditors(node);
        });
    });

    // Configure MutationObserver options
    const observerOptions = {
        childList: true,
        subtree: true,
    };

    // Selects the parent element where the events occur
    const mainContent = document.body;

    // Starts to observe the selected father element with the configured options
    observer.observe(mainContent, observerOptions);
});
