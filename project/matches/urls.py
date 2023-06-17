from django.urls import path
from . import views
from django.urls import path

app_name = 'matches'

urlpatterns = [
    path('', views.matches),
    path('selectteam', views.selectteam)
]