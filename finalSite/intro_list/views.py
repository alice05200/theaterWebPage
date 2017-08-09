from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, redirect
from django.http import Http404, HttpResponseRedirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
def index(request):
    return render_to_response('finalapp/index.html', locals())
def QandA(request):
    return render_to_response('intro_list/QandA.html', locals())
def aboutus(request):
    return render_to_response('intro_list/about.html', locals())
def contact(request):
    if request.method == 'GET':
        forms = ContactForm()
        return render(request, 'intro_list/contact.html', {'forms': forms})
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            email = forms.cleaned_data['email']
            phonenumber = forms.cleaned_data['phonenumber']
            content = forms.cleaned_data['content']
            Contact.objects.create(name=name, email=email, phonenumber=phonenumber, content=content)
            return render_to_response('intro_list/contactOK.html', locals())
        else:
            return render(request, 'intro_list/contact.html', {'forms': forms})
    
def contactSend(request):
    return render_to_response('intro_list/contactOK.html', locals())
def device(request):
    return render_to_response('intro_list/device.html', locals())
