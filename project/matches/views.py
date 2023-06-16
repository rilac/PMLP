from django.shortcuts import render

# Create your views here.
def matches(request):
    return render(request, '../templates/matches/matches.html')

def selectteam(request):
    return render(request, '../templates/selectteam/selectteam.html')