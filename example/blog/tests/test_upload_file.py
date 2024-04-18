from django.test import override_settings
from django.urls import reverse


def test_upload_file(admin_client, image_png):
    with image_png as upload:
        response = admin_client.post(
            reverse("ck_editors_upload_image"),
            {"upload": upload},
        )
    assert response.status_code == 200
    assert "url" in response.json()


@override_settings(
    CKEDITORS_FILE_STORAGE="storages.backends.gcloud.GoogleCloudStorage",
    GS_BUCKET_NAME="test",
)
def test_upload_file_to_google_cloud(admin_client, image_png, settings):
    with image_png as upload:
        response = admin_client.post(
            reverse("ck_editors_upload_image"),
            {"upload": upload},
        )
    assert response.status_code == 200
    assert "url" in response.json()
