from django.urls import path

from . import views

urlpatterns = [
    path("image_upload/", views.upload_file, name="ck_editors_upload_file"),
]
