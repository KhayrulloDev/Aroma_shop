# Generated by Django 4.2.5 on 2023-10-11 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_description_en_product_description_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
    ]
