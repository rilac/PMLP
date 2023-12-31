from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home),
    path('matches/', include('matches.urls')),
    path('virtualmatch/', include('virtualmatch.urls')),
    path('board/', include('board.urls')),
    path('signin/', views.signin),
    path('userinfo/', views.userinfo),
    path('signup/', include('memberlist.urls')),
    path('register/', include('memberlist.urls')),
]

