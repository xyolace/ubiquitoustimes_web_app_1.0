# Generated by Django 4.2.5 on 2024-01-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('xyolace_app', '0034_delete_a0_page_logo_delete_a0_page_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='A0PAGELOGO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='Page Logo')),
            ],
        ),
        migrations.CreateModel(
            name='A0PAGETITLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
            ],
        ),
    ]