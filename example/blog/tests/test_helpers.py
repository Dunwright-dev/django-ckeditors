import os
import shutil

import pytest
from django.conf import settings
from django.contrib.auth.models import AnonymousUser

# from django.core.files.storage import Storage
# from django.core.files import uploadedfile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, SimpleTestCase, override_settings

from django_ckeditors.exceptions import (
    InvalidImageTypeError,
)
from django_ckeditors.helpers import (
    handle_uploaded_image,
    has_permission_to_upload_images,
    image_verify,
)
from django_ckeditors.image import convert_image_to_webp


class TestHasPermissionToUploadImages(SimpleTestCase):
    def test_non_staff_user_has_permision_to_upload_image(self):
        request = RequestFactory().get("/")
        request.user = AnonymousUser()  # Simulate a non-authenticated user
        assert (
            has_permission_to_upload_images(request) is True
        )  # Should have permission

    @override_settings(
        DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS=True,
    )
    def test_non_staff_user_no_permision_to_upload_image(self):
        request = RequestFactory().get("/")
        request.user = AnonymousUser()  # Simulate a non-authenticated user
        assert (
            has_permission_to_upload_images(request) is False
        )  # Should have permission


class TestImageVerify(SimpleTestCase):
    def test_invalid_filetype(self):
        """invalid_jpg_image is a pdf file with jpg extension."""
        with open("../fixtures/files/images/this_is_a_pdf_file.jpg", "rb") as f:
            uploaded_file = SimpleUploadedFile("test_corrupted.png", f.read())

        with pytest.raises(InvalidImageTypeError):
            image_verify(uploaded_file)

    def test_valid_filetypes(self):
        with open("../fixtures/files/images/test_image.jpg", "rb") as f:
            uploaded_file = SimpleUploadedFile("test_corrupted.png", f.read())

        assert image_verify(uploaded_file) is None


class HandleUploadedImageTests(SimpleTestCase):
    @override_settings(
        DJ_CKE_FORMAT_IMAGE=False,
        DJ_CKE_IMAGE_STORAGE="",
        STORAGES={
            "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        },
    )
    def test_default_upload_url_no_image_formatting(self):
        # Create test image data
        with open("../fixtures/files/images/test_image.jpg", "rb") as f:
            uploaded_file = SimpleUploadedFile("test_image.jpg", f.read())

        # Create request with the test image
        request = RequestFactory().post("/", {"upload": uploaded_file})

        result_url = handle_uploaded_image(request)
        assert result_url == settings.MEDIA_URL + "test_image.jpg"

    @override_settings(
        DJ_CKE_FORMAT_IMAGE=True,
        DJ_CKE_IMAGE_STORAGE="",
        STORAGES={
            "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        },
    )
    def test_default_upload_url_default_image_formatting(self):
        # Create test image data
        with open("../fixtures/files/images/test_image.jpg", "rb") as f:
            uploaded_file = SimpleUploadedFile("test_image.jpg", f.read())

        # Create request with the test image
        request = RequestFactory().post("/", {"upload": uploaded_file})
        file_name, _ = convert_image_to_webp(uploaded_file)
        result_url = handle_uploaded_image(request)
        assert result_url == f"{settings.MEDIA_URL}{file_name}"

    @override_settings(
        DJ_CKE_FORMAT_IMAGE=False,
        DJ_CKE_IMAGE_STORAGE="blog.storage.ImageCustomFileSystemStorage",
        STORAGES={
            "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        },
    )
    def test_image_custom_file_storage_upload_no_image_formatting(self):
        # Create test image data
        with open("../fixtures/files/images/test_image.jpg", "rb") as f:
            uploaded_file = SimpleUploadedFile("test_image.jpg", f.read())

        # Create request with the test image
        request = RequestFactory().post("/", {"upload": uploaded_file})

        result_url = handle_uploaded_image(request)
        assert result_url == f"tests/custom/path/{uploaded_file.name}"

    @override_settings(
        DJ_CKE_FORMAT_IMAGE=True,
        DJ_CKE_IMAGE_STORAGE="blog.storage.ImageCustomFileSystemStorage",
        STORAGES={
            "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        },
    )
    def test_image_custom_file_storage_upload_default_image_formatting(self):
        with open("../fixtures/files/images/test_image.jpg", "rb") as f:
            uploaded_file = SimpleUploadedFile("test_image.jpg", f.read())
        # Create request with the test image
        request = RequestFactory().post("/", {"upload": uploaded_file})

        file_name, _ = convert_image_to_webp(uploaded_file)
        result_url = handle_uploaded_image(request)
        assert result_url == f"tests/custom/path/{file_name}"

    def tearDown(self):
        """
        Overriding the TearDown function from TestCase for deleting the test file
        """

        folder = settings.MEDIA_ROOT
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if "test" in file_path:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
            # try:
            #     shutil.rmtree(settings.MEDIA_ROOT + "/tests/")

            except FileNotFoundError:
                pass  # File might have not been created in the test
