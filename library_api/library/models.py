from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True)
    country = models.CharField(max_length=50, default="Kenya")

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publication_date = models.DateField(null=True)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="review")
    rating = models.CharField(default=3)
    comment = models.TextField(default="A really good book to read")

    def __str__(self):
        return f"{self.book} - {self.rating}/5"


