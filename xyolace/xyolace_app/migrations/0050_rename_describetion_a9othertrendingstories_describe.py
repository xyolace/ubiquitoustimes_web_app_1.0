# Generated by Django 4.2.5 on 2024-01-30 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0049_rename_a10oldothertrendingtopstory_b1oldothertrendingtopstory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='a9othertrendingstories',
            old_name='Describetion',
            new_name='Describe',
        ),
    ]