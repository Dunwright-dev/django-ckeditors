import os

import pytest

from django_ckeditors.fields import CKEditorsField
from django_ckeditors.forms import UploadFileForm


@pytest.fixture()
def valid_png_image():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        "files",
        "images",
        "test.png",
    )
    return open(file_path, "rb")


@pytest.fixture()
def invalid_jpg_image():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        "files",
        "images",
        "this_is_a_pdf_file.jpg",
    )
    return open(file_path, "rb")


@pytest.fixture()
def corrupted_png_image():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        "files",
        "images",
        "test_corrupted.png",
    )
    return open(file_path, "rb")


@pytest.fixture()
def ckeditors_field():
    return CKEditorsField()


@pytest.fixture()
def upload_file_form():
    return UploadFileForm()
