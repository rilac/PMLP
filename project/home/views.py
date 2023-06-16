from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, '../templates/home/index.html')

def signin(request):
    return render(request, '../templates/sign/login.html')