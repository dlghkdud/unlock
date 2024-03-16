from django.shortcuts import render, redirect

import os
from django.conf import settings

def index(request):
    return render(request, 'unlockk/start.html')

def signup(request):
    return render(request, 'unlockk/signup.html')

def signin(request):
    return render(request, 'unlockk/signin.html')