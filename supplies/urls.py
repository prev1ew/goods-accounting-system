from django.contrib import admin
from django.urls import path, include
from .views import supplies_hpage


urlpatterns = [
    path('', supplies_hpage, name='supplies'),
]
