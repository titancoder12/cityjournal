from django.contrib import admin
from django.urls import path, include
from .views import JournalEntries

urlpatterns = [
    path('', JournalEntries)
    #path('', getData),
]