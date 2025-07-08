from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to bolg home page')

# Create your views here.
