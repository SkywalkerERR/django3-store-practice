# Generated by Django 5.0.6 on 2024-07-10 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_basker_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
    ]