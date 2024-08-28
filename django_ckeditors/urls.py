from django.urls import path

from . import views

urlpatterns = [
    path(
        "image_upload/",
        views.upload_image,
        name="ck_editors_upload_image",
    ),
    # path(
    #     "unused_image_upload/",
    #     views.upload_image,
    #     name="ck_editors_unused_upload_image",
    # ),
]
