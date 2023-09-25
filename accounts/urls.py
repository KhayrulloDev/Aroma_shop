from django.urls import path

from main.views import HomeView, BlogView, CategoryView,ConfirmationView,ContactView,CheckoutView,ShoppingView

urlpatterns = [
    path('', HomeView.as_view()),
    path('blog', BlogView.as_view()),
    path('category', CategoryView.as_view()),
    path('checkout', CheckoutView.as_view()),
    path('contact', ContactView.as_view()),
    path('shop', ShoppingView.as_view()),
    path('confirmation', ConfirmationView.as_view()),
]