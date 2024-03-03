from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('credentials:login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save();
                return redirect('credentials:login')

        else:
            messages.info(request, 'password not matched')
            return redirect('credentials:register')
        print('user created')
        return redirect('/')

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')


