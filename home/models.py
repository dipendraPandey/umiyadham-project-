from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    FieldPanel,
    StreamFieldPanel,

)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField

from wagtail.core.models import Page
from wagtail.contrib.table_block.blocks import TableBlock
from . import Blocks


# ###################  This is the Model for Home Page ################## @dipendra
class HomePage(Page):
    max_count = 1
    template = "home/home_page.html"
    # the below subpage is responsible for how many types of page can be created under Home page
    # subpage_types = []
    parent_page_types = ["wagtailcore.Page"]
    banner_title = models.CharField(max_length=120, blank=False, null=True)
    banner_subtitle = RichTextField(features=['bold', 'italic'], blank=True, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    body = RichTextField(blank=True)
    content = StreamField(
        [
            ("Full_RichText",Blocks.RichtextBLock()),
            ("Title_Text", Blocks.TitleAndTextBlock()),
            ("Button", Blocks.ButtonBlock()),
            ("Cards", Blocks.CardBlock()),
            ("Image_gallery", Blocks.ImageGallery()),
        ],
        blank=True,
        null=True,
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('banner_title'),
            FieldPanel('banner_subtitle'),
            ImageChooserPanel('banner_image'),

        ], heading="banner content"),
        FieldPanel('body', classname="full"),
        StreamFieldPanel("content")

    ]


class EventCreation(Page):
    template = "event_and_news/event_creation.html"
    event_title = models.CharField(max_length=250, blank=False)
    event_description = StreamField(
        [
            ("Full_RichText", Blocks.RichtextBLock()),
            ("Table", Blocks.CreateTable()),
            ("Gallery", Blocks.ImageGallery()),
            ("Title_text", Blocks.TitleAndTextBlock()),
            ("Button", Blocks.ButtonBlock()),
        ], help_text="Event description",
    )
    event_history = StreamField(
        [
            ("Full_RichText", Blocks.RichtextBLock()),
            ("Title_and_Text", Blocks.TitleAndTextBlock()),
            ("Gallery", Blocks.ImageGallery()),
        ]
    )
    event_completion = models.BooleanField(blank=False, default=False)
    panels = [
        FieldPanel('event_title'),
        StreamFieldPanel('event_description'),
        FieldPanel('event_completion')
    ]


class NewsCreation(Page):
    template = "event_and_news/news_creation.html"
    news_title = models.CharField(max_length=250, blank=False)
    news_description = StreamField(
        [
            ("Full_RichText", Blocks.RichtextBLock()),
            ("Table", Blocks.CreateTable()),
            ("Gallery", Blocks.ImageGallery()),
            ("Title_text", Blocks.TitleAndTextBlock()),
            ("Button", Blocks.ButtonBlock()),
        ], help_text="News description",
    )
    panels = [
        FieldPanel('news_title'),
        StreamFieldPanel("news_description"),
             ]


# ############ This is the Flexible page model ########## @dipendra
class FlexiblePage(Page):
    template = "home/flexible_page.html"
    page_subtitle = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        help_text="You can provide subtitle to Page")
    new_table_options = {
        'minSpareRows': 0,
        'startRows': 2,
        'startCols': 2,
        'colHeaders': False,
        'rowHeaders': False,
        'contextMenu': True,
        'editor': 'text',
        'stretchH': 'all',
        'height': 216,
        'language': 'en',
        'renderer': 'text',
        'autoColumnSize': False,
    }
    content = StreamField(
        [
            ("Full_RichText", Blocks.RichtextBLock()),
            ("Title_Text", Blocks.TitleAndTextBlock()),
            ("Button", Blocks.ButtonBlock()),
            ("Cards", Blocks.CardBlock()),
            ("Image_gallery", Blocks.ImageGallery()),
            ("Table", TableBlock()),
        ]
    )
    content_panels = Page.content_panels + [
        FieldPanel("page_subtitle"),
        StreamFieldPanel("content")
    ]
