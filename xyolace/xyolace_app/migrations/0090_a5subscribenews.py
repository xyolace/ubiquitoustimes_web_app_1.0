# Generated by Django 4.2.5 on 2024-02-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0089_a4hotpicks_remove_a3newstoday_head'),
    ]

    operations = [
        migrations.CreateModel(
            name='A5SUBSCRIBENEWS',
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
