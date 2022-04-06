from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

def home_page(request):
    template_name = 'home.html'
    context = {
        'Hello': 'Hello'
    }
    return render(request, template_name, context=context)


    