from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
# !1!from django.contrib import messages


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            # !1! else :
            # !1!    messages.ERROR(request, "Username Or Password is not valid")  
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

# Create your views here.
