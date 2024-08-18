from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import JournalEntry
from .serializers import GroupSerializer, UserSerializer, JournalEntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows journal entries to be viewed or edited.
    """
    queryset = JournalEntry.objects.all().order_by('title')
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]