from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            try:
                user = authenticate(request, username=User.objects.get(email=username), password=password)
            except:
                user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Username Or Password is not valid")  
        return render(request,'accounts/login.html')
    else:
        return redirect('/')
@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')
    #if request.user.is_authenticated:
    #    logout(request)
    #return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login')

        form = UserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else :
        return redirect('/')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

def password_change_done(request):
    return render(request, 'accounts/password_change_done.html')
# Create your views here.
