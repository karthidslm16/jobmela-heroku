from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound  

def show(request):  
    return render(request, 'home.html')