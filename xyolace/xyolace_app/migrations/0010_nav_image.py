# Generated by Django 4.2.5 on 2024-01-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0009_rename_link_after_basic_nav_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='nav_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True)),
                ('title_image', models.ImageField(null=True, upload_to='navlogo')),
                ('image', models.ImageField(null=True, upload_to='navlogo')),
            ],
        ),
    ]
