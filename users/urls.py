from django.urls import path

from users.views import render_register_user, \
    process_register_user, render_login, process_login


app_name = 'users'

urlpatterns = [
    path('new/', render_register_user, name='new'),
    path('register/', process_register_user, name='register'),
    path('login/', render_login, name='login'),
    path('authorize/', process_login, name='authorize'),
]
