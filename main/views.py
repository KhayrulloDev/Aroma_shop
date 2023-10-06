from typing import Union
from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView

from .models import Product, Picture


class HomeView(View):

    def get(self, request):
        return render(request, 'index.html')


class CategoryView(View):
    tempalate_name = 'category.html'
    context = {}

    def get(self, request):
        products = Product.objects.all()
        product_data = []
        for product in products:
            image = Picture.objects.filter(product=product).first()
            product.image = image
            product_data.append(product)
        self.context.update({'products': product_data})
        return render(request, self.tempalate_name, self.context)


class BlogView(View):

    def get(self, request):
        return render(request, 'blog.html')


class ShoppingView(View):

    def get(self, request):
        return render(request, 'cart.html')


class CheckoutView(View):

    def get(self, request):
        return render(request, 'checkout.html')


class ConfirmationView(View):

    def get(self, request):
        return render(request, 'confirmation.html')


class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')


class SingleProductView(View):
    def post(self, request):
        product_id = request.GET.get('id')
        product = Product.objects.get(id=product_id)
        return render(request, 'single-product.html', {'product': product})

class AddProductView(CreateView):
    model = Product
    template_name = 'add_product.html'
    fields = ('name', 'price', 'description')


class TrackingOrderView(CreateView):

    def get(self, request):
        return render(request, 'tracking-order.html')
