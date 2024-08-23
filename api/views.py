from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action, api_view

@api_view(['GET'])
def JournalEntries(request):
    queryset = JournalEntry.objects.all()
    serializer = JournalEntrySerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)

#@api_view(['GET'])
#def getData(request):
#    person = {
#        'name': 'John Doe',
#        'age': 29,
#        'city': 'New York'
#    }
#    return Response(person)
# TEST STRING
# test 2