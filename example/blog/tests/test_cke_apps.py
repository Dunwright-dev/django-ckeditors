from unittest.mock import patch  # Import the 'patch' decorator

from django.conf import settings
from django.test import SimpleTestCase

from django_ckeditors.apps import DjangoCKEditorsConfig


class TestDjangoCKEditorsSettingsConfig(SimpleTestCase):
    def test_dj_cke_csrf_cookie_name_defaults_to_csrf_cookie_name(self):
        # default setting
        assert settings.DJ_CKE_CSRF_COOKIE_NAME == settings.CSRF_COOKIE_NAME

    def test_dj_cke_csrf_cookie_name_uses_user_override(self):
        # user setting
        with patch.object(settings, "DJ_CKE_CSRF_COOKIE_NAME", "user_cookie_name"):
            DjangoCKEditorsConfig.ready(self)
            assert settings.DJ_CKE_CSRF_COOKIE_NAME == "user_cookie_name"

    def test_dj_cke_custom_colour_pallette_default_setting(self):
        # default setting
        assert "color" in list(
            settings.DJ_CKE_CUSTOM_COLOUR_PALETTE[0].keys(),
        )
        assert "label" in list(
            settings.DJ_CKE_CUSTOM_COLOUR_PALETTE[0].keys(),
        )

    def test_dj_cke_custom_colour_pallette_uses_user_override(self):
        # user setting
        with patch.object(
            settings,
            "DJ_CKE_CUSTOM_COLOUR_PALETTE",
            [{"color": "hsl(207, 90%, 54%)", "label": "Blue"}],
        ):
            DjangoCKEditorsConfig.ready(self)
            assert [
                {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
            ] == settings.DJ_CKE_CUSTOM_COLOUR_PALETTE

    def test_dj_cke_custom_css_default_setting(self):
        # default setting
        assert settings.DJ_CKE_CUSTOM_CSS == ""

    def test_dj_cke_custom_css_uses_user_override(self):
        # user setting
        with patch.object(settings, "DJ_CKE_CUSTOM_CSS", "custom.css"):
            DjangoCKEditorsConfig.ready(self)
            assert settings.DJ_CKE_CUSTOM_CSS == "custom.css"

    def test_dj_cke_image_url_handler_default_setting(self):
        # default setting
        assert settings.DJ_CKE_IMAGE_URL_HANDLER == ""

    def test_dj_cke_image_url_handler_uses_user_override(self):
        # user setting
        with patch.object(settings, "DJ_CKE_IMAGE_URL_HANDLER", "custom.image.handler"):
            DjangoCKEditorsConfig.ready(self)
            assert settings.DJ_CKE_IMAGE_URL_HANDLER == "custom.image.handler"

    def test_dj_cke_image_storage_default_setting(self):
        # default setting
        assert settings.DJ_CKE_IMAGE_STORAGE == ""

    def test_dj_cke_image_storage_uses_user_override(self):
        # user setting
        with patch.object(settings, "DJ_CKE_IMAGE_STORAGE", "custom.image.storage"):
            DjangoCKEditorsConfig.ready(self)
            assert settings.DJ_CKE_IMAGE_STORAGE == "custom.image.storage"

    def test_dj_cke_permitted_image_types_default_setting(self):
        # default setting
        assert [
            "jpg",
            "jpeg",
            "png",
            "gif",
            "bmp",
            "webp",
            "tiff",
        ] == settings.DJ_CKE_PERMITTED_IMAGE_TYPES

    def test_dj_cke_permitted_image_types_uses_user_override(self):
        # user setting
        with patch.object(settings, "DJ_CKE_PERMITTED_IMAGE_TYPES", ["xyz", "abc"]):
            DjangoCKEditorsConfig.ready(self)
            assert ["xyz", "abc"] == settings.DJ_CKE_PERMITTED_IMAGE_TYPES

    def test_dj_cke_staff_only_image_uploads_default_setting(self):
        # default setting
        assert settings.DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS is False

    def test_dj_cke_staff_only_image_uploads_uses_user_override(self):
        # user setting
        with patch.object(settings, "DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS", new=True):
            DjangoCKEditorsConfig.ready(self)
            assert settings.DJ_CKE_STAFF_ONLY_IMAGE_UPLOADS is True

    def test_dj_cke_editors_configs_default_setting(self):
        # default setting
        keys = settings.DJ_CKE_EDITORS_CONFIGS.keys()
        assert "default" in keys
        assert "extends" in keys

    def test_dj_cke_editors_configs_uses_user_override(self):
        # user setting
        with patch.object(settings, "DJ_CKE_EDITORS_CONFIGS", {"a": 1, "b": 2}):
            DjangoCKEditorsConfig.ready(self)
            assert {"a": 1, "b": 2} == settings.DJ_CKE_EDITORS_CONFIGS
