from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
<<<<<<< HEAD
    path('journalentries/', views.journal_entries.as_view()),
    path('journalentry/', views.journal_entry.as_view()),
    path('images/', views.images.as_view()),
    path('register/', views.register_user.as_view(), name='register_user'),
    path('login/', views.login_user.as_view(), name='login_user'),
    path('logout/', views.logout_user.as_view(), name='logout_user'),
=======
    path('journalentries/', views.journal_entries, name='journal_entries'),
    path('journalentry/', views.journal_entry, name='journal_entry'),
    path('images/', views.images, name='images'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
>>>>>>> origin/christopher
]