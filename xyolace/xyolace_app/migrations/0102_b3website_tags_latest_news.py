# Generated by Django 4.2.5 on 2024-02-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0101_b3website_tags_alter_b2storeads_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='b3website_tags',
            name='Latest_news',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
