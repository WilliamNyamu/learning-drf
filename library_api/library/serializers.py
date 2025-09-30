from rest_framework import serializers
from .models import Author, Book, Review

class ReviewSerializer(serializers.ModelSerializer):
    # StringRelatedField is read-only. That’s why in POST, you can’t provide the book anymore(IF YOU USE IT) → DRF ignores it.
    # book = serializers.StringRelatedField()
    book_title = serializers.CharField(source="book.title", read_only = True)
    class Meta:
        model = Review
        fields = ['id', 'book', 'book_title','rating', 'comment']
    
    def validate(self, attrs):
        if int(attrs['rating']) > 5:
            raise serializers.ValidationError("Rating is between 1-5")
        return attrs
        
class BookSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publication_date', 'isbn', 'price', 'review')

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('id', 'name','bio', 'books', 'country')


