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
        1. CKEDITORS_FILE_STORAGE setting.
        2. DEFAULT_FILE_STORAGE
        3. STORAGES['default']

    :returns The imported storage class:

    :raises ImproperlyConfigured: If no valid storage class configuration is found.
    """
    storage_setting = getattr(settings, "CKEDITORS_FILE_STORAGE", None)
    default_storage_setting = getattr(settings, "DEFAULT_FILE_STORAGE", None)
    storages_setting = getattr(settings, "STORAGES", {})
    default_storage_name = storages_setting.get("default", {}).get("BACKEND")

    # Explanation: import_string allows us to import a class dynamically
    # based on its name as a string within settings.
    if storage_setting:
        return import_string(storage_setting)

    if default_storage_setting:
        try:
            return import_string(default_storage_setting)
        except ImportError as e:
            error_msg = f"Invalid default storage class: {default_storage_setting}"
            raise ImproperlyConfigured(error_msg) from e
    elif default_storage_name:
        try:
            return import_string(default_storage_name)
        except ImportError as e:
            error_msg = f"Invalid default storage class: {default_storage_name}"
            raise ImproperlyConfigured(error_msg) from e
    else: # No valid configuration found
        error_msg = (
            "Either CKEDITORS_FILE_STORAGE, DEFAULT_FILE_STORAGE, "
            "or STORAGES['default'] setting is required."
        )
        raise ImproperlyConfigured(error_msg)

storage = get_storage_class()

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

    if hasattr(settings,"DJ_CKE_PERMITTED_IMAGE_TYPES"):

        permitted_image_types: list = settings.DJ_CKE_PERMITTED_IMAGE_TYPES

    else:
        # Fallback to CKEditor 5 default image types
        permitted_image_types: list = ["jpeg", "png", "gif", "bmp", "webp", "tiff"]

    kind = filetype.guess(image)
    if kind is None or kind.extension not in permitted_image_types:
        error_msg = "Invalid image type, valid types [ 'jpeg', 'png', 'gif', 'bmp', 'webp', 'tiff' ]"
        logger.error(error_msg )
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

def handle_uploaded_file(f):
    fs = storage()
    filename = fs.save(f.name, f)
    return fs.url(filename)


def has_permission_to_upload_images(request)->bool:

    has_perms = True
    if hasattr(settings,  "DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS") and (
            settings.DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS
    ) and not request.user.is_staff:
        has_perms = False

    return has_perms
