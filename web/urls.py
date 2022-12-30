from django.urls import path
from django.contrib.auth.views import logout_then_login
from .views import (
    index, terms, privacy, 
    user_login, user_register, 
    user_dashboard, user_create,
    manager_dashboard, 
)

urlpatterns = [
    path(r'', index, name='index'),
    path(r'terms', terms, name='terms'),
    path(r'privacy', privacy, name='privacy'),
    path(r'login', user_login, name='login'),
    path(r'logout', logout_then_login, name='logout'),
    path(r'register', user_register, name='register'),
    path(r'management', manager_dashboard, name='manager_dashboard'),
    path(r'dashboard', user_dashboard, name='user_dashboard'),
    path(r'dashboard', user_create, name='user_add'),
]
