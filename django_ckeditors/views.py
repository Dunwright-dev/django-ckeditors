"""django-ckeditors views."""

import logging

from django import get_version
from django.http import Http404

from django_ckeditors.exceptions import (
    InvalidImageTypeError,
    PillowImageError,
)
from django_ckeditors.helpers import has_permission_to_upload_images

if get_version() >= "4.0":
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _

from django.http import JsonResponse

from django_ckeditors.forms import UploadFileForm
from django_ckeditors.helpers import (
    handle_uploaded_image,
    image_verify,
)

logger = logging.getLogger(__name__)


def upload_image(request):

    if not has_permission_to_upload_images(request) or (
            request.method != "POST"):
        raise Http404(_("Page not found."))

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        try:
            image_verify(request.FILES["upload"])
        except PillowImageError as e:
            return JsonResponse({"error": {"message": f"{e}"}})
        except InvalidImageTypeError as e:
            return JsonResponse({"error": {"message": f"{e}"}})
        if form.is_valid():
            url = handle_uploaded_image(request)
            return JsonResponse({"url": url})
        else:
            return JsonResponse({"error": form.errors})

    return JsonResponse({"error": {"message": "An unknown error occurred"}})
