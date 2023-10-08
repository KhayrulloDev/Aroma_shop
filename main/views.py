from typing import Union
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.db.models import Q
from .models import Product, Picture, Korzinka
from .utils import increment_count, decrement_count
import json
from django.http import JsonResponse


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

    def post(self, request):
        id = request.POST.get('id')
        user_id = request.user.id
        card = Korzinka.objects.create(
            product_id=id,
            user_id=user_id
        )
        card.save()
        messages.info(request, 'Added successfully!')
        return redirect('/shopping_cart')


class BlogView(View):

    def get(self, request):
        return render(request, 'blog.html')


class ShoppingView(View):
    tempalate_name = 'cart.html'
    context = {}

    def get(self, request):
        shopping_cart = Korzinka.objects.filter(user=request.user).values('product_id')
        products = Product.objects.filter(pk__in=shopping_cart)
        data = []
        for product in products:
            shop = Korzinka.objects.get(Q(user=request.user, product=product))
            product.count = shop.count
            data.append(product)
        self.context.update({'products': data})
        return render(request, 'cart.html', self.context)

    def post(self, request):
        id = request.POST.get('id')
        user = request.user
        shopping_cart = Korzinka.objects.get(Q(product_id=id) & Q(user=user))
        shopping_cart.delete()
        return redirect('/shopping_cart')


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


class IncrementCountView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            id = json_data.get('id')
        except json.JSONDecodeError:
            id = None
        result = increment_count(id, request.user)
        return JsonResponse({'result': result})


class DecrementCountView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            id = json_data.get('id')
        except json.JSONDecodeError:
            id = None
        result = decrement_count(id, request.user)
        return JsonResponse({'result': result})


class AddProductsView(View):
    model = Product
    template_name = 'add_products.html'
