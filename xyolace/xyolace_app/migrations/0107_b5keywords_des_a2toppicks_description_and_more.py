# Generated by Django 4.2.5 on 2024-02-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0106_a3newstoday_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='B5KEYWORDS_DES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MAINPAGEKEYWORD', models.CharField(max_length=150)),
                ('MAINPAGEDESCRIPTION', models.TextField()),
                ('HOTPAGEKEYWORD', models.CharField(max_length=150)),
                ('HOTPAGEDESCRIPTION', models.TextField()),
                ('TOPPAGEKEYWORD', models.CharField(max_length=150)),
                ('TOPPAGEDESCRIPTION', models.TextField()),
                ('LATESTPAGEKEYWORD', models.CharField(max_length=150)),
                ('LATESTPAGEDESCRIPTION', models.TextField()),
                ('SPORTSPAGEKEYWORD', models.CharField(max_length=150)),
                ('SPORTSPAGEDESCRIPTION', models.TextField()),
                ('ECONOMICSPAGEKEYWORD', models.CharField(max_length=150)),
                ('ECONOMICSPAGEDESCRIPTION', models.TextField()),
                ('LIFESTYLEPAGEKEYWORD', models.CharField(max_length=150)),
                ('LIFESTYLEPAGEDESCRIPTION', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='a2toppicks',
            name='Description',
            field=models.TextField(default='k'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a2toppicks',
            name='KEYWORD',
            field=models.CharField(default='k', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a3newstoday',
            name='Description',
            field=models.TextField(default='l'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a3newstoday',
            name='KEYWORD',
            field=models.CharField(default='l', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a4hotpicks',
            name='Description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a4hotpicks',
            name='KEYWORD',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a6othernews',
            name='Description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a6othernews',
            name='KEYWORD',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a7ecoandworld',
            name='Description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a7ecoandworld',
            name='KEYWORD',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a8lifestyle',
            name='Description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='a8lifestyle',
            name='KEYWORD',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
