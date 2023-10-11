from modeltranslation.translator import TranslationOptions, translator

from main.models import Product


class ProductTranslation(TranslationOptions):
    fields = ('name', 'category' ,'description')


translator.register(Product, ProductTranslation)
