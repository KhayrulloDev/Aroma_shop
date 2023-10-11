from django import forms
from multiupload.fields import MultiImageField

from main.models import Category

category_names = Category.objects.values_list('name', flat=True)


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FloatField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ProductForm(forms.Form):
    name2 = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter product name',
    }))
    category = forms.ModelChoiceField(label='Category', queryset=category_names, widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'Choose category'
    }))
    price = forms.FloatField(label='Price', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter product price'
    }))
    image = MultiImageField(min_num=1, max_num=10, max_file_size=1024*1024*5, required=True)
    description = forms.CharField(label='description', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Description'
    }))
