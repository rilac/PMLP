from django.urls import path
from . import views
from django.urls import path, include

app_name = 'virtualmatch'

urlpatterns = [
    path('', views.virtualmatch),
]