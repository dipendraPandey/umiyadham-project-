from django.db import models
# from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel


# Create your models here.
class MenuItem(Orderable):
    link_title = models.CharField(max_length=50, blank=True, null=True)
    link_url = models.CharField(max_length=500, blank=True, )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)
    page = ParentalKey("Menu", related_name="menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    # @todo add property
    @property
    def link(self):
        if self.link_url:
            return self.link_url
        elif self.link_page:
            return self.link_page.url
        else:
            return "#"

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return "Missing Title"


@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=120)
    # slug = AutoSlugField(populate_from="title", editable = True)
    slug = models.SlugField()

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("title"),
                FieldPanel("slug"),
            ], heading="menu"
        ),
        InlinePanel("menu_items", label='Menu item'),

    ]

    def __str__(self):
        return self.title


class NavigationImage(Orderable):
    nvimage = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        help_text="select Image",
        on_delete=models.SET_NULL,
        related_name='+',
    )

    page = ParentalKey("NavImage", related_name="nav_image")
    panels = [
         ImageChooserPanel('nvimage'),
              ]


@register_snippet
class NavImage(ClusterableModel):
    title = models.CharField(max_length=120, blank=False)
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("title",),
                InlinePanel("nav_image", max_num=2, min_num=1),

            ], heading="Nav Image"
        ),
    ]

    def __str__(self):
        return self.title
