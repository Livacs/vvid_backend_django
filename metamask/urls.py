from django.urls import path
from . import views

urlpatterns = [
    path('auth-web3/', views.auth_web3, name='auth_web3'),
    path('', views.index)
    
]
