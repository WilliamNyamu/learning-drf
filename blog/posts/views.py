from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from django.contrib.auth.models import User
from rest_framework import filters
# Create your views here.

class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'last_name']

class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
