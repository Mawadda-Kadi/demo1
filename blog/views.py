from django.shortcuts import render
from djando.http import httpResponse

def home(request):
    return httpResponse('Welcome to bolg home page')

# Create your views here.
