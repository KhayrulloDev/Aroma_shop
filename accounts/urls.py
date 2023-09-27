from django.urls import path

from .views import SignInView, RegisterView

urlpatterns = [
    path('sign-in', SignInView.as_view()),
    path('register', RegisterView.as_view()),
]