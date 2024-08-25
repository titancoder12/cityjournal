from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('journalentries/', views.journal_entries, name='journal_entries'),
    path('journalentry/', views.journal_entry, name='journal_entry'),
    path('images/', views.images, name='images'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]