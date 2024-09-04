from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('journalentries/', views.journal_entries.as_view()),
    path('journalentry/', views.journal_entry.as_view()),
    path('images/', views.images.as_view()),
    path('register/', views.register_user.as_view(), name='register_user'),
    path('login/', views.login_user.as_view(), name='login_user'),
    path('logout/', views.logout_user.as_view(), name='logout_user'),
]