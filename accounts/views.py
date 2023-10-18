from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login


def login_view(request):
    if request.user.is_authenticated:
        msg = f'user is authenticated as {request.user.username}'
    else :
        msg = 'user is not authenticated'
    
    
    return render(request,'accounts/login.html',{'msg':msg})

def logout_view(request):
    return redirect('/')

def signup_view(request):
    return render(request,'accounts/signup.html')

# Create your views here.
