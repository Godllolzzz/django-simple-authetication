from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='loginpage')
def HomePage(request):
    return render(request, 'home.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'login.html', {
                'hasError' : True
            })
            # return HttpResponse('Username or password in incorrect')

    if request.method == 'GET':
        return render(request, 'login.html', {
            'hasError' : False
        })

def LogoutPage(request):
    logout(request)
    return redirect('loginpage')

def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return HttpResponse("password and confirm password does not match")
        else:
            user = User.objects.create_user(username, email, password1)
            user.set_password(password1)
            return redirect('loginpage')

    if request.method == 'GET':
        return render(request, 'signup.html')
