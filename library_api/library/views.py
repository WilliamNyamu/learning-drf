from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author, Review
from .serializers import BookSerializer, AuthorSerializer, ReviewSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookCreateListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RetrieveAndUpdateAndDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        # Starts with the base queryset from the class
        queryset = Book.objects.all()
        # Looks for a query parameter named 'name' in the request's URL.
        # self.request.query_params is a dictionary-like object
        title_filter = self.request.query_params.get('title', None)
        if title_filter is not None:
            queryset = queryset.filter(title__icontains=title_filter)
            # title__icontains=title_filter is a lookup function
                # title -> the model field you're seraching in
                # __icontains -> a lookup that means:
                    # i = case-insensitive
                    # contains = substring match
        return queryset

class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains = name_filter)
        return queryset

class ReviewAPIView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    





        

