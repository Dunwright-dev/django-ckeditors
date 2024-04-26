"""django-ckeditor helpers."""

import logging

import filetype
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string
from PIL import Image, UnidentifiedImageError
from PIL.Image import DecompressionBombError

from django_ckeditors.exceptions import (
    InvalidImageTypeError,
    PillowImageError,
)

logger = logging.getLogger(__name__)


def get_storage_class():
    """
    Determines the appropriate storage class for CKEditors based on settings.

    This function searches through a prioritized set of Django settings
    to dynamically determine the storage class to be used.

    Priority Order:
        1. DJ_CKE_FILE_STORAGE setting.
        2. DEFAULT_FILE_STORAGE
        3. STORAGES['default']

    :returns The imported storage class:

    :raises ImproperlyConfigured: If no valid storage class configuration is found.
    """
    # We can directly call DJ_CKE_IMAGE_STORAGE because it is always available.
    dj_cke_img_storage_setting = settings.DJ_CKE_IMAGE_STORAGE
    default_storage_setting = getattr(settings, "DEFAULT_FILE_STORAGE", None)
    storages_setting = getattr(settings, "STORAGES", {})
    default_storage_name = storages_setting.get("default", {}).get("BACKEND")

    storage_class: str = ""

    # Explanation: import_string allows us to import a class dynamically
    # based on its name as a string within settings.

    if dj_cke_img_storage_setting:
        storage_class = dj_cke_img_storage_setting
    elif default_storage_setting:
        storage_class = default_storage_setting
    elif default_storage_name:
        storage_class = default_storage_name
    try:
        return _get_storage_object(storage_class)
    except ImproperlyConfigured as e:
        logger.exception({e.args[0]})
        raise ImproperlyConfigured from e


def _get_storage_object(storage_class: str = ""):
    try:
        storage = import_string(storage_class)
        return storage()
    except ImportError as e:
        error_msg = (
            "Either DJ_CKE_IMAGE_STORAGE, DEFAULT_FILE_STORAGE, "
            "or STORAGES['default'] setting is required."
        )
        raise ImproperlyConfigured(error_msg) from e


def image_verify(image):
    """Verifies whether an image file is valid and has a supported type.

    Validates an image file and ensures it falls within the permitted image
    types. The function checks for potential corruption, decompression bombs,
    and unsupported file formats.

    :param image: The image file to verify. An image file-like object or a filename.
    :type image: file-like object or str
    :raises PillowImageError: If the image is corrupt, too large, or cannot be verified.
    :raises InvalidImageTypeError: If the image has an unsupported file type.
    """

    # Fallback to `CKEditor 5` default image types if not set.
    permitted_image_types = settings.DJ_CKE_PERMITTED_IMAGE_TYPES

    kind = filetype.guess(image)
    if kind is None or kind.extension not in permitted_image_types:
        error_msg = (
            "Invalid image type, valid types "
            "[ 'jpeg', 'png', 'gif', 'bmp', 'webp', 'tiff' ]"
        )
        logger.error(error_msg)
        raise InvalidImageTypeError(error_msg)


    try:
        Image.open(image).verify()
    except FileNotFoundError as e:
        error_msg = "This image file is not valid or corrupted."
        logger.exception(
            error_msg,
        )
        raise PillowImageError(error_msg, e) from e
    except UnidentifiedImageError as e:
        error_msg = "This image file is corrupted."
        logger.exception(
            error_msg,
        )
        raise PillowImageError(error_msg, e) from e
    except DecompressionBombError as e:
        error_msg = "This image file is corrupted or to large to use."
        logger.exception(
            error_msg,
        )
        raise PillowImageError(error_msg, e) from e


def handle_uploaded_image(request):
    """Handles an uploaded image, saving it to storage and returning its URL.

    Leverages a custom URL handler if specified in Django settings.

    :param request: (HttpRequest) The Django request object containing the
        uploaded file.
        Available in `request.FILES["upload"]`

    :returns: (URL) The URL where the uploaded image is stored.
    """

    try:
        storage = get_storage_class()
    except ImproperlyConfigured:
        error_msg = "A valid storage system has not been configured"
        logger.exception(error_msg)
        # .. todo:: Return json response with errors.
        return error_msg

    img = request.FILES["upload"]  # Extract the uploaded image file

    # Check for a custom URL handler in Django setting
    custom_url_handler = getattr(settings, "DJ_CKE_IMAGE_URL_HANDLER", None)
    if custom_url_handler:
        url_handler = import_string(custom_url_handler)
        url = url_handler(request)  # Get the URL using the custom handler

    else:

        url = img.name  # Default to using the image's filename as the URL

    filename = storage.save(name=url, content=img)

    return storage.url(filename)  # Return the URL of the saved image


def has_permission_to_upload_images(request) -> bool:

    has_perms = True
    if (
        hasattr(settings, "DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS")
        and (settings.DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS)
        and not request.user.is_staff
    ):
        has_perms = False

    return has_perms
