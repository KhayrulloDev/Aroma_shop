from django.urls import path

from .views import (HomeView, CategoryView, BlogView,
                    ShoppingView, CheckoutView,
                    ConfirmationView, ContactView,
                    TrackingOrderView
                    )

urlpatterns = [
    path('', HomeView.as_view()),
    path('category', CategoryView.as_view(), name='category'),
    path('blog', BlogView.as_view(), name='blog'),
    path('shopping_cart', ShoppingView.as_view(), name='cart'),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('confirmation', ConfirmationView.as_view(), name='conf'),
    path('contact', ContactView.as_view(), name='contact'),
    path('tracking-order', TrackingOrderView.as_view(), name='tracking')
]
