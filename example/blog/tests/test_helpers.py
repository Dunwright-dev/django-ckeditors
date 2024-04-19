from unittest.mock import MagicMock, patch

import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory

from django_ckeditors.exceptions import InvalidImageTypeError, PillowImageError
from django_ckeditors.helpers import has_permission_to_upload_images, image_verify


class TestHasPermissionToUploadImages:
    @staticmethod
    def test_non_staff_user_without_setting():
        request = RequestFactory().get("/")
        request.user = AnonymousUser()  # Simulate a non-authenticated user

        assert (
            has_permission_to_upload_images(request) is True
        )  # Should have permission

    @staticmethod
    @patch("django.conf.settings.DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS", new=True)
    def test_non_staff_user_with_setting():
        request = RequestFactory().get("/")
        request.user = AnonymousUser()

        assert has_permission_to_upload_images(request) is False

    @staticmethod
    @patch("django.conf.settings.DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS", new=True)
    def test_staff_user():
        request = RequestFactory().get("/")
        request.user = MagicMock(is_staff=True)  # Simulate staff user

        assert has_permission_to_upload_images(request) is True


class TestImageVerify:
    @staticmethod
    def test_valid_filetype(valid_png_image):

        image_verify(image=valid_png_image)  # Should execute without raising exceptions

    @staticmethod
    def test_invalid_filetypes(invalid_jpg_image):
        """invalid_jpg_image is a pdf file with jpg extension."""

        with pytest.raises(InvalidImageTypeError):
            image_verify(invalid_jpg_image)

    @staticmethod
    def test_corrupt_png(corrupted_png_image):
        """corrupted_png_image is a png with random bytes changed."""
        with pytest.raises(PillowImageError):
            image_verify(corrupted_png_image)
