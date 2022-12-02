from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    # Copy-pasted as-is from official tutorial.
    # See https://docs.wagtail.org/en/stable/getting_started/tutorial.html#extend-the-homepage-model.
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
