
Django CKEditors |Docs| |Django| |Repo|
=======================================
|

**Version = 2025.05.22.3**

|

    **CKEditor 5 Integration for Django >= 2.0**

    Vendored from this excellent project: https://github.com/hvlads/django-ckeditor-5

|

Licenses
--------

|

    **Django:** BSD 3-Clause "New" or "Revised" License

    **CKEditor 5:** GPL 2+ copyleft license

|

What is django-ckeditors
------------------------

django-ckeditors: A Powerful and Versatile Rich Text Editor for Your Django Projects

* Seamlessly integrate the renowned CKEditor 5 into your Django website.
* Provide your users with a modern and intuitive content creation experience.
* Includes features like text formatting, image uploads, tables, code blocks, and more.
* Highly customizable to fit your project's exact needs.

"django-ckeditor-5 provides a strong foundation, and I'm building upon it with customizations that align perfectly with my project's needs."

|

See the Quickstart: `here <https://django-ckeditors.readthedocs.io/en/latest/how-to/quickstart.html>`__

|

Ideal For:
~~~~~~~~~~


    * Blogs
    * Content Management Systems (CMS)
    * Websites requiring advanced text editing features


Includes the following CKEditor 5 plugins
-----------------------------------------

* **Text Formatting**
    * **Basic:**
        * Bold
        * Italic
        * Underline
        * Strikethrough
        * Superscript
        * Subscript
        * Code
    * **Paragraph and Structure:**
        * BlockQuote
        * Heading
        * Paragraph
        * Alignment

    * **Lists:**
        * List
        * TodoList
        * ListProperties

    * **Advanced:**
        * Highlight
        * Indent
        * IndentBlock


* **Images and Media**
    * **Core:**
        * Image
        * ImageCaption
        * ImageStyle
        * ImageToolbar
        * ImageResize
        * ImageInsert
        * LinkImage

    * **Upload:**
        * UploadAdapter
        * SimpleUploadAdapter

    * **Embedding:**
        * MediaEmbed
        * HtmlEmbed

* **Other**
    * **Link:**
        * Link

    * **Table:**
        * Table
        * TableToolbar
        * TableCaption
        * TableProperties
        * TableCellProperties

    * **Style:**
        * Font
        * Style
        * HorizontalLine

    * **Editing Tools:**
        * CodeBlock
        * Autoformat
        * PasteFromOffice
        * RemoveFormat
        * SourceEditing
        * GeneralHtmlSupport

    * **Word Processing Features**
        * WordCount
        * Mention

|


Optimizing Bundle Size
----------------------

|

By default, django-ckeditors includes all available languages. If you only need specific languages, you can create a custom build:

1. Clone this repository
2. Modify `webpack.config.mjs`:

.. code-block:: javascript

    new CKEditorTranslationsPlugin({
        language: 'en', // This is the main language, you can change this to suit

        // and or
        additionalLanguages: ['es', 'fr'], // Only languages you need
        // additionalLanguages: 'all',

        buildAllTranslationsToSeparateFiles: true,
    }),

3.  Run `npm run prod` to build with only your required languages.


.. code-block:: bash

    npm run prod


|

.. |Docs| image:: https://readthedocs.org/projects/django-ckeditors/badge/?version=latest
    :target: https://django-ckeditors.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. |Django| image:: https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FimAsparky%2Fdjango-ckeditors%2Fmain%2Fpyproject.toml&query=project.dependencies&logo=Django&label=Versions&labelColor=%23092E20
   :target: https://docs.djangoproject.com/en/4.2/
   :alt: Django Version Badge
.. |Repo| image:: https://www.repostatus.org/badges/latest/wip.svg
   :target: https://www.repostatus.org/#wip
   :alt: Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.