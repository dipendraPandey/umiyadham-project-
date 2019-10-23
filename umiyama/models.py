from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
        FieldPanel,
        MultiFieldPanel,
        RichTextFieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel


# Create your models here.


class UmiyaMaaPage(Page):
    template = "umiyama/umiya_maa_page.html"
    max_count = 1
    parent_page_types = ["home.HomePage"]
    sub_page_types = ["umiyama.CreateMaaPage"]
    custom_title = models.CharField(max_length=30, blank=False, null=True, help_text="Enter the title Fore the page")
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        """adding custom stuff to context """
        context = super().get_context(request, *args, **kwargs)
        all_pages = CreateMaaPage.objects.live().public()
        context["pages"] = all_pages
        return context


class CreateMaaPage(Page):
    template = "umiyama/create_maa_page.html"
    parent_page_types = ["umiyama.UmiyaMaaPage"]
    sub_page_types = []
    maa_name = models.CharField(max_length=120, blank=False, null=True)
    maa_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Please select the Image ",
    )
    maa_description = RichTextField(blank=False, null=True, help_text="Fill the field")
    content_panels = Page.content_panels + [
        FieldPanel("maa_name"),
        ImageChooserPanel("maa_image"),
        FieldPanel("maa_description")

    ]


class MasterPage(Page):
    parent_page_types = ['home.HomePage']
    subtitle = models.CharField(max_length=120, blank=True, null=True, help_text="Give subtitle to the page")

    content_panels = Page.content_panels + [
        FieldPanel("subtitle")
    ]





