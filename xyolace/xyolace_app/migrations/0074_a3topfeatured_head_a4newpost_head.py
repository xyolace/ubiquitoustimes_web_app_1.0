# Generated by Django 4.2.5 on 2024-02-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0073_delete_a8latestnews_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='a3topfeatured',
            name='Head',
            field=models.CharField(default='Top Picks', max_length=100),
        ),
        migrations.AddField(
            model_name='a4newpost',
            name='Head',
            field=models.CharField(default='Top News Today', max_length=100),
        ),
    ]
