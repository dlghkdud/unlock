from django.shortcuts import render

def index(request):
    return render(request, 'unlockk/start.html')