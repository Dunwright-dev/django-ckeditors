from django_ckeditors.widgets import CKEditorsWidget


def test_ckeditor5_field_internal_type(ckeditors_field):
    assert ckeditors_field.get_internal_type() == "TextField"


def test_ckeditor5_field_formfield(ckeditors_field):
    formfield = ckeditors_field.formfield()
    assert formfield.max_length == ckeditors_field.max_length
    assert isinstance(formfield.widget, CKEditorsWidget)
