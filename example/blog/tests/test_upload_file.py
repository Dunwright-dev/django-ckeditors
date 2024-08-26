"""test only staff can upload file"""

from django.test import override_settings
from django.urls import reverse


@override_settings(
    DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS=True,
)
def test_upload_file(admin_client, valid_png_image):
    with valid_png_image as upload:
        response = admin_client.post(
            reverse("ck_editors_upload_image"),
            {"upload": upload},
        )
    assert response.status_code == 200
    assert "url" in response.json()


# @override_settings(
#     DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS=True,
#     DJ_CKE_IMAGE_STORAGE="storages.backends.gcloud.GoogleCloudStorage",
#     GS_BUCKET_NAME="test",
# )
# def test_upload_file_to_google_cloud(admin_client, valid_png_image, settings):
#     with valid_png_image as upload:
#         response = admin_client.post(
#             reverse("ck_editors_upload_image"),
#             {"upload": upload},
#         )
#     assert response.status_code == 200
#     assert "url" in response.json()
