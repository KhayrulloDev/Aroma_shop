from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model, hashers, authenticate, login, logout
from django.contrib import messages

User = get_user_model()


class SignInView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Username or password is incorrect")
            return redirect('/account/login')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect('/account/register')
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('/account/register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password1
                )
                user.save()
                return redirect('/account/login')

        else:
            messages.error(request, "Passwords are not same!!")
            return redirect('/account/register')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')
