from django.urls import path

from stock.views import create_dish, process_create_dish, \
    menu, pre_purchases

app_name = 'stock'

urlpatterns = [
    path('create/', create_dish, name='create-dish'),
    path('process-dish/', process_create_dish, name='process-dishes'),
    path('menu/<int:user_pk>/', menu, name='menu'),
    path('pre-purchases/<int:user_pk>', pre_purchases, name='pre-purchases'),
]
