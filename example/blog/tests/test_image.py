from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from PIL import Image

from django_ckeditors.image import convert_image_to_webp


class ImageConversionTests(TestCase):
    def test_jpeg_conversion(self):
        with open(
            # "../fixtures/files/images/test_image.jpg",
            "../fixtures/files/images/test_image.jpg",
            "rb",
        ) as f:
            uploaded_file = SimpleUploadedFile("test_image.jpg", f.read())
        webp_filename, image_stream = convert_image_to_webp(uploaded_file)
        self.assertEqual(webp_filename, "test_image.webp")

        # Verify WEBP format and image content
        image = Image.open(image_stream)
        self.assertEqual(image.format, "WEBP")
        self.assertEqual(image.mode, "RGB")

    def test_png_conversion(self):
        with open("../fixtures/files/images/test_image.png", "rb") as f:
            uploaded_file = SimpleUploadedFile("test_image.png", f.read())

        webp_filename, image_stream = convert_image_to_webp(uploaded_file)
        self.assertEqual(webp_filename, "test_image.webp")

        # Verify WEBP format and image content
        image = Image.open(image_stream)
        self.assertEqual(image.format, "WEBP")
        self.assertEqual(image.mode, "RGB")

    def test_animated_gif_conversion(self):
        with open(
            "../fixtures/files/images/test_image.gif", "rb"
        ) as f:  # Replace with a test GIF
            uploaded_file = SimpleUploadedFile("test_image.gif", f.read())

        webp_filename, image_stream = convert_image_to_webp(uploaded_file)
        self.assertEqual(webp_filename, "test_image.webp")

        # Verify WEBP format, image content, and animation
        image = Image.open(image_stream)
        self.assertEqual(image.format, "WEBP")
        self.assertEqual(image.mode, "RGB")

    def test_large_image_quality_adjustment(self):
        # Create a large test image
        large_image = Image.new("RGB", (13300, 13400))
        image_stream = BytesIO()
        large_image.save(image_stream, format="JPEG")
        image_stream.seek(0)
        uploaded_file = SimpleUploadedFile("large_image.jpg", image_stream.getvalue())

        # Call the conversion function and check if quality is reduced
        _, image_stream = convert_image_to_webp(uploaded_file)

        converted_file = SimpleUploadedFile("image.webp", image_stream.getvalue())
        self.assertLess(converted_file.size, uploaded_file.size / 8)
