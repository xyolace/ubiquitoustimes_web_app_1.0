# Generated by Django 4.2.5 on 2024-01-14 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0003_menuitem_dropdownitem_deepdropdownitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dropdownitem',
            name='parent_menu',
        ),
        migrations.DeleteModel(
            name='DeepDropdownItem',
        ),
        migrations.DeleteModel(
            name='DropdownItem',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]