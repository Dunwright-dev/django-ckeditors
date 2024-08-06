from django.db import models

from .widgets import CKEditorsWidget


class CKEditorsField(models.TextField):
    def __init__(self, *args, toolbar_config="default", **kwargs) -> None:
        self.toolbar_config = toolbar_config
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        # Extract and analyze the provided widget
        admin_calling = False
        widget = kwargs.get("widget", None)
        # INFO: This is to let the widget know
        # that the js needs to be included for admin.
        if "django.contrib.admin.widgets" in str(widget):
            admin_calling = True

        return super().formfield(
            **{
                "max_length": self.max_length,
                **(
                    {
                        "widget": CKEditorsWidget(
                            admin_calling=admin_calling,
                            toolbar_config=self.toolbar_config,
                        ),
                    }
                ),
                **kwargs,
            },
        )
