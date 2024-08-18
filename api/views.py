from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import JournalEntry
from .serializers import GroupSerializer, UserSerializer, JournalEntrySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


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

    def get_queryset(self):
        queryset = JournalEntry.objects.all().order_by('title')
        limit = self.request.query_params.get('limit', None)
        if limit is not None:
            try:
                limit = int(limit)
                queryset = queryset[:limit]
            except ValueError:
                pass  # If limit is not an integer, ignore it
        return queryset
    
    @action(detail=False, methods=['get'], url_path='get_by_id')
    def get_by_id(self, request):
        journal_entry_id = request.query_params.get('id', None)
        if journal_entry_id is not None:
            try:
                journal_entry = JournalEntry.objects.get(id=journal_entry_id)
                serializer = JournalEntrySerializer(journal_entry)
                return Response(serializer.data)
            except JournalEntry.DoesNotExist:
                return Response({'error': 'JournalEntry not found'}, status=404)
        return Response({'error': 'ID parameter is required'}, status=400)
#class JournalEntryViewSet(viewsets.ModelViewSet)