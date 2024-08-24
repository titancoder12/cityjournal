from .models import JournalEntry, Image
from .serializers import JournalEntrySerializer, ImageSerializer, UserRegistrationSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_user(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def journal_entries(request):
    limit = int(request.query_params.get('limit', len(JournalEntry.objects.all())))
    id = request.user.id
    entries = JournalEntry.objects.filter(id=id).order_by('-date')[:limit]
    if not bool(entries):
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = JournalEntrySerializer(entries, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def journal_entry(request):
    if request.method == 'GET':
        id = request.query_params.get('id', None)
        if id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            entry = JournalEntry.objects.get(id=id)
        except JournalEntry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = JournalEntrySerializer(entry, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = JournalEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def images(request):
    if request.method == 'GET':
        entry_id = request.query_params.get("entry_id", None)
        if entry_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            images = Image.objects.filter(entry_id=entry_id)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ImageSerializer(images, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = JournalEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action, api_view, authentication_classes, permission_classes

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
# TEST 103847329847 123 STRING
# test 2