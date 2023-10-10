from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import (HomeView, CategoryView, BlogView,
                    ShoppingView, CheckoutView,
                    ConfirmationView, ContactView,
                    TrackingOrderView, SingleProductView,
                    IncrementCountView, DecrementCountView,
                    AddProductsView
                    )

urlpatterns = [
    path('', HomeView.as_view()),
    path('category', CategoryView.as_view(), name='category'),
    path('blog', BlogView.as_view(), name='blog'),
    path('shopping_cart', ShoppingView.as_view(), name='cart'),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('confirmation', ConfirmationView.as_view(), name='conf'),
    path('contact', ContactView.as_view(), name='contact'),
    path('tracking-order', TrackingOrderView.as_view(), name='tracking'),
    path('single-product', SingleProductView.as_view(), name='single-product'),
    path('increment-count', csrf_exempt(IncrementCountView.as_view()), name='increment-count'),
    path('decrement-count', csrf_exempt(DecrementCountView.as_view()), name='decrement-count'),
    path('add-product', AddProductsView.as_view(), name='add-product'),
]
