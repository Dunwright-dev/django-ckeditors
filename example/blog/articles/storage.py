import os
from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class CustomStorage(FileSystemStorage):
    """Custom storage for django_ckeditors images."""

    location = os.path.join(settings.MEDIA_ROOT, "django_ckeditors")
    base_url = urljoin(settings.MEDIA_URL, "django_ckeditors/")
