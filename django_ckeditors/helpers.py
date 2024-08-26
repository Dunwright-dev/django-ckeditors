"""django-ckeditor helpers."""

import logging

import filetype
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string
from PIL import Image, UnidentifiedImageError

from django_ckeditors.exceptions import (
    InvalidImageTypeError,
    PillowImageError,
)
from django_ckeditors.image import convert_image_to_webp

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

    # import_string allows us to import a class dynamically
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

    # Fallback to `CKEditors` default image types if not set.
    permitted_image_types = settings.DJ_CKE_PERMITTED_IMAGE_TYPES
    # filetype checks the file, not just the extension.
    kind = filetype.guess(image)
    if kind is None or kind.extension.lower() not in permitted_image_types:
        error_msg = (
            f"Invalid image type, valid types {permitted_image_types}\n"
            f"It seems you have uploaded a '{kind.extension}' filetype!"
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
    except Image.DecompressionBombError as e:
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
    image = request.FILES["upload"]  # Extract the uploaded image file
    try:
        storage = get_storage_class()
    except ImproperlyConfigured:
        error_msg = "A valid storage system has not been configured"
        logger.exception(error_msg)
        return error_msg

    # Get image and URL handlers
    if getattr(settings, "DJ_CKE_IMAGE_FORMATTER", None):
        convert_image = import_string(settings.DJ_CKE_IMAGE_FORMATTER)
    else:
        convert_image = convert_image_to_webp
    if getattr(settings, "DJ_CKE_IMAGE_URL_HANDLER", None):
        get_image_url_and_optionally_save = import_string(
            settings.DJ_CKE_IMAGE_URL_HANDLER,
        )
    else:
        get_image_url_and_optionally_save = None

    if settings.DJ_CKE_FORMAT_IMAGE and convert_image:
        file_name, image = convert_image(image)
    else:
        file_name = image.name

    # Set up to optionally save/return url to cke text editor.
    if get_image_url_and_optionally_save:
        image_url, img_saved = get_image_url_and_optionally_save(
            request,
            file_name,
            image,
        )
    else:
        img_saved = False
        image_url = file_name

    if not img_saved:
        filename = storage.save(name=image_url, content=image)
        image_url = storage.url(filename)
    return image_url  # Return the saved image URL to the cke editor


def has_permission_to_upload_images(request) -> bool:
    """
    Checks if the user  has permission to upload images.

    Args:
        request (django.http.HttpRequest): The HTTP request object representing
        the user's interaction.

    Returns:
        bool: True if the user has permission to upload images, False otherwise.

    Behavior:
        - By default, all users have permission to upload images.
        - If the Django setting `DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS` is set to True,
          only staff users will have permission.
    """
    has_perms = True
    if (
        hasattr(settings, "DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS")
        and (settings.DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS)
        and not request.user.is_staff
    ):
        has_perms = False

    return has_perms
