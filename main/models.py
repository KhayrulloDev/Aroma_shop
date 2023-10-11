from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from typing import Union

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=155)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_date = models.DateTimeField(auto_now_add=True)

    def create(self, validated_data):
        print(validated_data)
        return super().save(**validated_data)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Picture(models.Model):
    image = models.ImageField(upload_to='pics')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Picture')
        verbose_name_plural = _('Pictures')


class Korzinka(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    uploaded = models.DateTimeField(auto_now_add=True)
