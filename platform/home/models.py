from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
    ]

    max_count = 1

    subpage_types = [
        "patterns.UrbanDesignPatternIndex",
        "resources.ResourcesIndex",
    ]
