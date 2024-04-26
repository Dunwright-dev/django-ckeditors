import os
import shutil

from django.conf import settings

# from django.core.files.storage import Storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, SimpleTestCase, override_settings

from django_ckeditors.helpers import (
    handle_uploaded_image,
)

# class TestHasPermissionToUploadImages:
#     @staticmethod
#     def test_non_staff_user_without_setting():
#         request = RequestFactory().get("/")
#         request.user = AnonymousUser()  # Simulate a non-authenticated user
#
#         assert (
#             has_permission_to_upload_images(request) is True
#         )  # Should have permission
#
#     @staticmethod
#     @patch("django.conf.settings.DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS", new=True)
#     def test_non_staff_user_with_setting():
#         request = RequestFactory().get("/")
#         request.user = AnonymousUser()
#
#         assert has_permission_to_upload_images(request) is False
#
#     @staticmethod
#     @patch("django.conf.settings.DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS", new=True)
#     def test_staff_user():
#         request = RequestFactory().get("/")
#         request.user = MagicMock(is_staff=True)  # Simulate staff user
#
#         assert has_permission_to_upload_images(request) is True
#
#
# class TestImageVerify:
#     @staticmethod
#     def test_valid_filetype(valid_png_image):
#
#         image_verify(image=valid_png_image)  # Should execute without raising exceptions  # noqa: E501
#
#     @staticmethod
#     def test_invalid_filetypes(invalid_jpg_image):
#         """invalid_jpg_image is a pdf file with jpg extension."""
#
#         with pytest.raises(InvalidImageTypeError):
#             image_verify(invalid_jpg_image)
#
#     @staticmethod
#     def test_corrupt_png(corrupted_png_image):
#         """corrupted_png_image is a png with random bytes changed."""
#         with pytest.raises(PillowImageError):
#             image_verify(corrupted_png_image)
#


class HandleUploadedImageTests(SimpleTestCase):
    @override_settings(
        DJ_CKE_IMAGE_STORAGE="",
        STORAGES={
            "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        },
    )
    def test_default_upload_url(self):
        # Create test image data
        image_data = b"Dummy image data"
        image_file = SimpleUploadedFile("test_image.jpg", image_data)

        # Create request with the test image
        request = RequestFactory().post("/", {"upload": image_file})

        result_url = handle_uploaded_image(request)
        assert result_url == settings.MEDIA_URL + "test_image.jpg"

    @override_settings(
        DJ_CKE_IMAGE_STORAGE="blog.storage.ImageCustomFileSystemStorage",
        STORAGES={
            "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        },
    )
    def test_image_custom_file_storage_upload(self):
        # Create test image data
        image_data = b"Dummy image data"
        image_file = SimpleUploadedFile("test_image.jpg", image_data)

        # Create request with the test image
        request = RequestFactory().post("/", {"upload": image_file})

        result_url = handle_uploaded_image(request)
        # assert 1 == 2
        assert result_url == f"tests/custom/path/{image_file.name}"

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
