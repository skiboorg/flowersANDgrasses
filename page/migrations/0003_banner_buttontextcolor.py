# Generated by Django 2.2.4 on 2019-09-23 21:13

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20190923_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='buttonTextColor',
            field=colorfield.fields.ColorField(default='#000000', max_length=18, verbose_name='Цвет текста кнопки'),
        ),
    ]
