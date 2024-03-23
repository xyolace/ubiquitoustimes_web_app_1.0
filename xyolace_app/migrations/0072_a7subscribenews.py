# Generated by Django 4.2.5 on 2024-02-05 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0071_delete_a7subscribenews'),
    ]

    operations = [
        migrations.CreateModel(
            name='A7SUBSCRIBENEWS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Subtitle', models.CharField(max_length=60, null=True)),
                ('Image', models.ImageField(null=True, upload_to='Subscribe News')),
                ('Text', models.TextField()),
                ('Button', models.CharField(max_length=40)),
            ],
        ),
    ]