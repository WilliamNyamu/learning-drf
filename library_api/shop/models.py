from django.db import models
from library.models import Author

# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=100)
    presenter = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="gifts")
    description = models.TextField()

    def __str__(self):
        return self.name

class Merchandise(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


