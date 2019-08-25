# Generated by Django 2.2.4 on 2019-08-25 16:43

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Категория')),
                ('name_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='category_img/', verbose_name='Изображение')),
                ('page_title', models.CharField(max_length=255, null=True, verbose_name='Название страницы')),
                ('page_description', models.CharField(max_length=255, null=True, verbose_name='Описание страницы')),
                ('page_keywords', models.TextField(null=True, verbose_name='Keywords')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание категории')),
                ('discount', models.IntegerField(blank=True, default=0, verbose_name='Скидка на все товары в категории %')),
                ('show_at_homepage', models.BooleanField(default=False, verbose_name='Отображать на главной?')),
                ('views', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название коллекции')),
                ('name_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='collection_img/', verbose_name='Изображение коллекции')),
                ('page_title', models.CharField(max_length=255, null=True, verbose_name='Название страницы')),
                ('page_description', models.TextField(null=True, verbose_name='Описание страницы')),
                ('page_keywords', models.TextField(null=True, verbose_name='Keywords')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание коллекции')),
                ('discount', models.IntegerField(blank=True, default=0, verbose_name='Скидка на все товары в коллекции %')),
                ('views', models.IntegerField(default=0)),
                ('show_at_homepage', models.BooleanField(default=True, verbose_name='Отображать на главной')),
                ('show_at_category', models.BooleanField(default=True, verbose_name='Отображать в категории')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название фильтра')),
                ('name_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.Category', verbose_name='Принадлежит категории')),
            ],
            options={
                'verbose_name': 'Фильтр',
                'verbose_name_plural': 'Фильтры',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название товара')),
                ('name_lower', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('name_slug', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('price', models.IntegerField(db_index=True, default=0, verbose_name='Цена')),
                ('page_title', models.CharField(max_length=255, null=True, verbose_name='Название страницы')),
                ('page_description', models.TextField(null=True, verbose_name='Описание страницы')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание товара')),
                ('article', models.CharField(max_length=50, null=True, verbose_name='Артикул')),
                ('color', models.CharField(blank=True, max_length=15, null=True, verbose_name='Цвет')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Отображать товар ?')),
                ('is_present', models.BooleanField(db_index=True, default=True, verbose_name='Товар в наличии ?')),
                ('discount', models.IntegerField(blank=True, default=0, verbose_name='Скидка')),
                ('buys', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.Category', verbose_name='В категории')),
                ('collection', models.ManyToManyField(blank=True, db_index=True, to='item.Collection', verbose_name='Коллекция')),
                ('filter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.Filter')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Промокод (для создания рандомного значения оставить пустым)')),
                ('promo_discount', models.IntegerField(default=0, verbose_name='Скидка на заказ')),
                ('use_counts', models.IntegerField(blank=True, default=1, verbose_name='Кол-во использований')),
                ('is_unlimited', models.BooleanField(default=False, verbose_name='Неограниченное кол-во использований')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен?')),
                ('expiry', models.DateTimeField(default=datetime.datetime(2019, 8, 25, 16, 43, 17, 968682), verbose_name='Срок действия безлимитного кода')),
            ],
            options={
                'verbose_name': 'Промокод',
                'verbose_name_plural': 'Промокоды',
            },
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='items', verbose_name='Изображение товара')),
                ('image_small', models.CharField(blank=True, default='', max_length=255)),
                ('is_main', models.BooleanField(default=False, verbose_name='Основная картинка ?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='item.Item', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Изображение для товара',
                'verbose_name_plural': 'Изображения для товара',
            },
        ),
    ]
