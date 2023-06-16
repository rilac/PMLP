from django.urls import path
from . import views
from django.urls import path, include

app_name = 'board'

urlpatterns = [
    path('', views.boardList),
]