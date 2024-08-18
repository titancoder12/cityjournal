from django.contrib.auth.models import Group, User
from . models import JournalEntry
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class  JournalEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  JournalEntry
        fields = ['url', 'title', 'location', 'body', 'user_id']