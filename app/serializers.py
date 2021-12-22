from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff')
        read_only_fields = ('is_staff', 'is_superuser')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ('id',)
        read_only_fields = ('created_at',)

class TopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top
        fields = ('id', 'name', 'image')
        read_only_fields = ['id']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'caption', 'picture')
        read_only_fields = ['id']

class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = ('id', 'title', 'picture')
        read_only_fields = ['id']
