from django.urls import path

from purchases.views import render_purchase


app_name = 'purchases'

urlpatterns = [
    path('purchase/', render_purchase, name='purchase'),
]
