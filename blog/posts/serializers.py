from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'full_name')
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".title()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
    

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'comments', 'publish_date', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()


    
    