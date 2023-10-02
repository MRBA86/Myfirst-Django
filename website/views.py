from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm , ContactForm , NewsletterForm

def index_view (request):
    return render(request,'website/index.html')

def about_view (request):
    return render(request,'website/about.html')

def contact_view (request):
    if request.method =='POST':
       form = ContactForm(request.POST)
       if form.is_valid():
           form.save()

    form = ContactForm()

    return render(request,'website/contact.html',{'form':form})

def newsletter_view (request):
    if request.method =='POST':
       form = NewsletterForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
    else :
        return HttpResponseRedirect('/')
        

    form = NewsletterForm()

    return render(request,'website/website.html',{'form':form})

def test_view (request):
    if request.method =='POST':
       form = ContactForm(request.POST)
       if form.is_valid():
           form.save()
           """ name = form.changed_data('name')
           subject =form.changed_data('subject')
           email = form.changed_data('email')
           message = form.changed_data('message')
           c = Contact()
           c.name = name
           c.subject = subject
           c.email = email
           c.message = message
           c.save() """
           return HttpResponse('DONE')
       else:
           return HttpResponse('NOT VALID')
    form = ContactForm()
    return render(request, 'test.html',{'form':form})
    
"""  name = request.POST.get('name')
        subject =request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        c = Contact()
        c.name = name
        c.subject = subject
        c.email = email
        c.message = message
c.save() """
    

# Create your views here.
