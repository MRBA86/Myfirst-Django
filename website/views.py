from django.shortcuts import render
from django.http import HttpResponse

def index_view (request):
    return HttpResponse('<h1> This Is Home Page <h1>')

def about_view (request):
    return HttpResponse('<h1> This Is About Page <h1>')

def contact_view (request):
    return HttpResponse('<h1> This Is Contact Page <h1>')

# Create your views here.
