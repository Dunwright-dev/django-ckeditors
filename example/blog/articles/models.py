from django.db import models

from django_ckeditors.fields import CKEditorsField


class Article(models.Model):
    """Articles for blog."""

    title = models.CharField("Title", max_length=200, null=True)
    text = CKEditorsField("Text", toolbar_config="extends")
    text2 = CKEditorsField("Text 2", toolbar_config="extends", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Articles"
        verbose_name = "Article"

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment for article."""

    author = models.CharField(max_length=250)
    text = CKEditorsField("Text")
    article = models.ForeignKey(
        Article,
        related_name="comments",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "Comments"
        verbose_name = "Comment"

    def __str__(self):
        return self.text
