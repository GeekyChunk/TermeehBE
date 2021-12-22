from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, views, authentication, status
from django.contrib.auth.models import User
from app.serializers import *
from app.models import *

# Create your views here.


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class CurrentUser(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
        
    def put(self, request, format=None):
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    permission_classes = (permissions.IsAdminUser|ReadOnly,)
    serializer_class = ItemSerializer

class ItemRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    permission_classes = (permissions.IsAdminUser|ReadOnly,)
    serializer_class = ItemSerializer
    lookup_field = 'slug'

class TopList(generics.ListCreateAPIView):
    queryset = Top.objects.all()
    serializer_class = TopSerializer
    permission_classes = (permissions.IsAdminUser|ReadOnly,)

class TopRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Top.objects.all()
    serializer_class = TopSerializer
    permission_classes = (permissions.IsAdminUser|ReadOnly,)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAdminUser|ReadOnly,)

class PostRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAdminUser|ReadOnly,)

class HighlightList(generics.ListCreateAPIView):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer
    permission_classes = (permissions.IsAdminUser|ReadOnly,)

class HighlightRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer
    permission_classes = (permissions.IsAdminUser|ReadOnly,)