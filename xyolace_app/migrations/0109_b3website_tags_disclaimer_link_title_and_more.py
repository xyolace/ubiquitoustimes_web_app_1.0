# Generated by Django 4.2.5 on 2024-04-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0108_remove_b3website_tags_facebook_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='b3website_tags',
            name='Disclaimer_link_title',
            field=models.CharField(default='copyright', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='b3website_tags',
            name='Disclaimer_link',
            field=models.URLField(),
        ),
    ]
