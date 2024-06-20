from django.db import models

from .widgets import CKEditorsWidget


class CKEditorsField(models.Field):
    def __init__(self, *args, toolbar_config="default", **kwargs) -> None:
        self.toolbar_config = toolbar_config
        super().__init__(*args, **kwargs)

    def get_internal_type(self) -> str:
        return "TextField"

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "max_length": self.max_length,
                **({"widget": CKEditorsWidget(toolbar_config=self.toolbar_config)}),
                **kwargs,
            },
        )
