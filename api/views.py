from .models import JournalEntry, Image
from .serializers import JournalEntrySerializer, ImageSerializer, UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserLoginSerializer
from rest_framework.views import APIView

#@api_view(['POST'])
#def register_user(request):
#    serializer = UserRegistrationSerializer(data=request.data)
#    if serializer.is_valid():
#        serializer.save()
#        return Response(serializer.data, status=status.HTTP_201_CREATED)
#    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class register_user(APIView):
    def get_serializer(self, *args, **kwargs):
        return UserRegistrationSerializer(*args, **kwargs)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['POST'])
#def login_user(request):
#    serializer = UserLoginSerializer(data=request.data)
#    if serializer.is_valid():
#        user = serializer.validated_data
#        token, created = Token.objects.get_or_create(user=user)
#        return Response({"token": token.key}, status=status.HTTP_200_OK)
#    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class login_user(APIView):
    def get_serializer(self, *args, **kwargs):
        return UserLoginSerializer(*args, **kwargs)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['POST'])
#def logout_user(request):
#    request.user.auth_token.delete()
#    return Response(status=status.HTTP_200_OK)

class logout_user(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

#@api_view(['GET'])
#def journal_entries(request):
#    limit = int(request.query_params.get('limit', len(JournalEntry.objects.all())))
#    id = request.user.id
#    entries = JournalEntry.objects.filter(id=id).order_by('-date')[:limit]
#    if not bool(entries):
#        return Response(status=status.HTTP_404_NOT_FOUND)
#    serializer = JournalEntrySerializer(entries, many=True, context={'request': request})
#    return Response(serializer.data)

class journal_entries(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        limit = int(request.query_params.get('limit', len(JournalEntry.objects.all())))
        id = request.user.id
        entries = JournalEntry.objects.filter(id=id).order_by('-date')[:limit]
        if not bool(entries):
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = JournalEntrySerializer(entries, many=True, context={'request': request})
        return Response(serializer.data)

#@api_view(['GET', 'POST'])
#def journal_entry(request):
#    if request.method == 'GET':
#        id = request.query_params.get('id', None)
#        if id is None:
#            return Response(status=status.HTTP_400_BAD_REQUEST)
#        try:
#            entry = JournalEntry.objects.get(id=id)
    #     except JournalEntry.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     serializer = JournalEntrySerializer(entry, context={'request': request})
    #     return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = JournalEntrySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class journal_entry(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer(self, *args, **kwargs):
        return JournalEntrySerializer(*args, **kwargs)

    def get(self, request):
        id = request.query_params.get('id', None)
        if id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            entry = JournalEntry.objects.get(id=id)
        except JournalEntry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(entry, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def images(request):
#     if request.method == 'GET':
#         entry_id = request.query_params.get("entry_id", None)
#         if entry_id is None:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         try:
#             images = Image.objects.filter(entry_id=entry_id)
#         except Image.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = ImageSerializer(images, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = JournalEntrySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class images(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer(self, *args, **kwargs):
        return ImageSerializer(*args, **kwargs)

    def get(self, request):
        entry_id = request.query_params.get("entry_id", None)
        if entry_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            images = Image.objects.filter(entry_id=entry_id)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(images, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)