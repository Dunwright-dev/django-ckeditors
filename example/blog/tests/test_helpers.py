from io import BytesIO
from unittest.mock import patch  # Or your favorite mocking library

import filetype
import pytest

from django_ckeditors.exceptions import InvalidImageTypeError
from django_ckeditors.helpers import image_verify


@patch("PIL.Image.open")  # Mock Image.open
def test_invalid_filetype(mock_image_open):
    mock_image_open.side_effect = lambda x: filetype.guess(x).extension == "pdf"

    # Simulate a PDF file's content
    fake_pdf_data = b"Dummy PDF file content"

    with pytest.raises(InvalidImageTypeError):
        image_verify(BytesIO(fake_pdf_data))


def test_valid_filetype(image_png):

    image_verify(image=image_png)  # Should execute without raising exceptions


@patch("filetype.guess")
def test_invalid_filetypes(mock_filetype):
    mock_filetype.return_value.extension = "pdf"  # Unsupported type

    with pytest.raises(InvalidImageTypeError):
        image_verify("./files/images/this_is_a_pdf_file.jpg")


#
# @patch("filetype.guess")
# @patch("PIL.Image.open")
# def test_pillow_error(mock_image_open, mock_filetype):
#     mock_filetype.return_value.extension = "jpg"
#     mock_image_open.side_effect = DecompressionBombError
#
#     # with open('./files/images/test.jpg', 'rb') as f:
#     with pytest.raises(PillowImageError):
#         image_verify("./files/images/test.jpg")


# @patch("PIL.Image.open")  # Mock the Image.open function
# def test_decompression_bomb(mock_image_open):
#     mock_image_open.side_effect = Image.DecompressionBombError(
#         "Simulated decompression error",
#     )
#
#     with pytest.raises(PillowImageError) as excinfo:  # Expect PillowImageError
#         image_verify("some_image.jpg")
#
#     assert "This image file is corrupted or too large to use." in str(excinfo.value)
#     assert isinstance(
#         excinfo.value.__cause__,
#         Image.DecompressionBombError,
#     )  # Check for chained exception
