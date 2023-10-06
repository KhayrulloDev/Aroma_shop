from django.urls import path

from .views import SignInView, RegisterView,LogoutView

urlpatterns = [
    path('login', SignInView.as_view()),
    path('register', RegisterView.as_view()),
    path('logout', LogoutView.as_view())
]