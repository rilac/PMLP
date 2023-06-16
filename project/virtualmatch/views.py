from django.shortcuts import render

# Create your views here.

def virtualmatch(request):
    return render(request, '../templates/virtualmatch/virtualmatch.html')