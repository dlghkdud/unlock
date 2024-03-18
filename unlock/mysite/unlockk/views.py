from django.shortcuts import render, redirect
from .models import Write

import os
from django.conf import settings

def index(request):
    return render(request, 'unlockk/start.html')

def signup(request):
    return render(request, 'common/signup.html')

def signin(request):
    return render(request, 'common/signin.html')

def picrew(request):
    return render(request, 'unlockk/picrew.html')

def home(request):
    return render(request, 'unlockk/home.html')