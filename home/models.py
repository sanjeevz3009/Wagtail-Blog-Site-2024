from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model
from wagtail.documents import get_document_model


class HomePage(Page):
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True)

    image = models.ForeignKey(
        get_image_model(),  # "wagtailimages.Image"
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    custom_document = models.ForeignKey(
        get_document_model(),  # "wagtaildocuments.Document"
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle", read_only=True),
        FieldPanel("body"),
        FieldPanel("image"),
        FieldPanel("custom_document"),
    ]
