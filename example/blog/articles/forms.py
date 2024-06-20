from django import forms

from django_ckeditors.widgets import CKEditorsWidget

from .models import Article, Comment


class CommentForm(forms.ModelForm):
    """Custom storage for django_ckeditors images."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = Comment
        fields = ("author", "text")
        widgets = {
            "text": CKEditorsWidget(
                attrs={"class": "django_ckeditors"},
                toolbar_config="comment",
            ),
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "text"]
        widgets = {
            "text": CKEditorsWidget(
                attrs={"class": "django_ckeditors"},
                toolbar_config="extends",
            ),
            "text2": CKEditorsWidget(
                attrs={"class": "django_ckeditors"},
                toolbar_config="default",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False
