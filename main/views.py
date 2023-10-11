from typing import Union
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .forms import ProductForm
from .models import Product, Picture, Korzinka, Category
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
        print(products)
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
        try:
            check_card = Korzinka.objects.get(user=request.user, product=id)
            # If a matching Korzinka object is found, you might want to update it here.
            # For example, you can increment the quantity.
            # check_card.quantity += 1
            # check_card.save()
            messages.info(request, 'Added successfully!')
            return redirect('/shopping_cart')
        except Korzinka.DoesNotExist:
            # Create a new Korzinka object if none exists for the user and product.
            card = Korzinka.objects.create(
                product_id=id,
                user_id=user_id
            )
            card.save()
            messages.info(request, 'Added successfully!')
            return redirect('/category')


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
            image = Picture.objects.filter(product=product).first()
            product.image = image
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


from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Picture  # Import your Product and Picture models


class SingleProductView(View):
    def get(self, request, pk):
        # Get the product based on the given primary key (pk)
        product = get_object_or_404(Product, pk=pk)

        # Get all images associated with the product (assuming you store multiple images for a product)
        images = Picture.objects.filter(product=product).all()

        print("Image >>>", images)
        # Pass the product and images to the template
        context = {
            'product': product,
            'images': images,
        }

        return render(request, 'single-product.html', context)


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


class AddProductView(View):
    form_class = ProductForm
    template_name = 'add_product.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name)

    def post(self, request):
        # form = self.form_class(request.POST, request.FILES)
        # print(form.data)


        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        description = request.POST.get('product_description')
        author = request.user  # Assuming request.user represents the product's author

        # Get the selected category (assuming you have a form field for category)
        category = Category.objects.filter(pk=request.POST.get('product_category')).first()

        # Create the Product object with all required fields set
        print(category)
        product = Product.objects.create(
            name=name,
            price=price,
            description=description,
            user=author,  # Change 'author' to 'user'
            category=category  # Set the category
        )

        images = request.FILES.getlist('product_image')  # Correctly access the uploaded files

        for image in images:
            picture = Picture.objects.create(
                image=image,
                product=product
            )
            picture.save()
        return redirect('/')

        # return render(request, self.template_name, {'form': form})
