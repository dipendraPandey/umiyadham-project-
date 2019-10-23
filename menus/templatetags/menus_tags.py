from django import template
from slugify import slugify

from ..models import Menu
from ..models import NavImage

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.get(slug=slug)


@register.simple_tag()
def all_menus():
    menu_list = []
    menus = Menu.objects.all().values_list('title')
    for item in range(len(menus)):

        title = menus[item][0]
        menu_list.append(slugify(title))

    return menu_list


# ######################## this template tag is for the nav_bar images ##@dipendra
@register.simple_tag()
def navimage():
    return NavImage.objects.all()

