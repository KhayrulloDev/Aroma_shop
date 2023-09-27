from django.shortcuts import render
from django.views import View


class HomeView(View):

    def get(self, request):
        return render(request, 'index.html')


class CategoryView(View):

    def get(self, request):
        return render(request, 'category.html')


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


