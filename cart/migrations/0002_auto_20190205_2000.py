# Generated by Django 2.1.5 on 2019-02-05 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customuser', '0001_initial'),
        ('cart', '0001_initial'),
        ('item', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='client',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Корзина клиента'),
        ),
        migrations.AddField(
            model_name='cart',
            name='guest',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='customuser.Guest', verbose_name='Корзина гостя'),
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='item.Item', verbose_name='Товар'),
        ),
    ]
