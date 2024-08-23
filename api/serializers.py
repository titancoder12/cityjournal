from django.contrib.auth.models import Group, User
from .models import JournalEntry
from rest_framework import serializers

class  JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model =  JournalEntry
        fields = '__all__'