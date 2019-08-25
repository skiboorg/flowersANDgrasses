# Generated by Django 2.2.4 on 2019-08-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1, verbose_name='Порядок отображения')),
                ('image', models.ImageField(upload_to='banners/', verbose_name='Картинка')),
                ('url', models.CharField(max_length=255, verbose_name='Ссылка на кнопке')),
                ('bigText', models.CharField(default='', max_length=255, verbose_name='Заголовок')),
                ('smallText', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('badgeText', models.CharField(blank=True, max_length=255, verbose_name='Текст в бейдже')),
                ('positionLeft', models.BooleanField(default=False, verbose_name='Текст слева?')),
                ('positionRight', models.BooleanField(default=True, verbose_name='Текст справа?')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
            },
        ),
    ]
