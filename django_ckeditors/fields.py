from django.db import models

from .widgets import CKEditorsWidget


class CKEditorsField(models.Field):
    def __init__(self, *args, config_name="default", **kwargs) -> None:
        self.config_name = config_name
        super().__init__(*args, **kwargs)

    def get_internal_type(self) -> str:
        return "TextField"

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "max_length": self.max_length,
                **({"widget": CKEditorsWidget(config_name=self.config_name)}),
                **kwargs,
            },
        )
