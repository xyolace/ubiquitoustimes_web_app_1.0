# Generated by Django 4.2.5 on 2024-02-23 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0085_a2top_picks_bgimage_alter_a2top_picks_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='a2top_picks',
            name='BGImage',
        ),
        migrations.RemoveField(
            model_name='a2top_picks',
            name='Head',
        ),
    ]
