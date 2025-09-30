from django.contrib import admin
from .models import Author, Book, Review
from django.contrib.admin import decorators

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
