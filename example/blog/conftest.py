import os

import pytest

from django_ckeditors.fields import CKEditorsField
from django_ckeditors.forms import UploadFileForm


@pytest.fixture()
def file():
    file_path = os.path.join(os.path.dirname(__file__), "fixtures", "files", "test.png")
    return open(file_path, "rb")


@pytest.fixture()
def ckeditors_field():
    return CKEditorsField()


@pytest.fixture()
def upload_file_form():
    return UploadFileForm()
