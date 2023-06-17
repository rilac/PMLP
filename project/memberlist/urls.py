from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('', views.signup),
    path('register/', views.joined, name='register'),

]