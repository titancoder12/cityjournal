from .models import JournalEntry, Image
from .serializers import JournalEntrySerializer, ImageSerializer, UserRegistrationSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status

"""
Register a new user
"""
@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Login a user
"""
@api_view(['POST'])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Logout a user
"""
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

"""
Get all journal entries for a current user
"""
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def journal_entries(request):
    limit = int(request.query_params.get('limit', len(JournalEntry.objects.all())))
    user_id = request.user.id
    entries = JournalEntry.objects.filter(user_id=user_id).order_by('-id')[:limit]
    print(entries)
    print(limit)

    if not bool(entries):
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = JournalEntrySerializer(entries, many=True, context={'request': request})
    return Response(serializer.data)

"""
Get a specific journal entry by id
"""
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def journal_entry(request):
    if request.method == 'GET':
        id = request.query_params.get('id', None)
        if id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            entry = JournalEntry.objects.get(id=id)
        except JournalEntry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            entry = JournalEntry.objects.get(id=id, user_id=request.user.id)
        except JournalEntry.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = JournalEntrySerializer(entry, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data.copy()
        data['user_id'] = request.user.id

        serializer = JournalEntrySerializer(data=data)
        
        #if request.user.id != data['user_id']:
        #    return Response(status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""
Get and add images for a given journal entry
"""
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def images(request):
    if request.method == 'GET':
        entry_id = request.query_params.get("entry_id", None)
        if entry_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            images = Image.objects.filter(entry_id=entry_id)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.user.id != images[0].entry.user_id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        serializer = ImageSerializer(images, many=True, context={'request': request})
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = ImageSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
