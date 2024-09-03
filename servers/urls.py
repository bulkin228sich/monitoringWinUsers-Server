"""
Definition of urls for servers.
"""


from django.urls import path

from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('info', views.info, name='info'),
    path('userinfo', views.userInfo, name='userinfo'),
    
]
