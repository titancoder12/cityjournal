from django.contrib import admin
from .models import JournalEntry, Image
# Register your models here.
admin.site.register(JournalEntry)
admin.site.register(Image)