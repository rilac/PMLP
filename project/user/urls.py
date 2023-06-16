from django.urls import path
from . import views
from django.urls import path, include

app_name = 'user'

urlpatterns = [
    path('', views.signup),

]