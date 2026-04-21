from django.db import models
from django.core.exceptions import ValidationError

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title

class Reader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE) # Un livre = une seule réservation active
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    date_reserved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} réservé par {self.reader.name}"