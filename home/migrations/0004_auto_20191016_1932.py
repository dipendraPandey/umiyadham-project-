# Generated by Django 2.2.6 on 2019-10-16 14:02

from django.db import migrations
import home.Blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191016_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('Full_RichText', home.Blocks.RichtextBLock()), ('Title_Text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your Title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional Text', required=True))])), ('Button', wagtail.core.blocks.StructBlock([('button_page', wagtail.core.blocks.PageChooserBlock(help_text='If this is selected the url will be of this page', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If page is not selected  this  url will work ', required=False))])), ('Cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('name', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('sub_name', wagtail.core.blocks.CharBlock(max_length=60, required=False)), ('text', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first', required=False))])))]))], blank=True, null=True),
        ),
    ]
