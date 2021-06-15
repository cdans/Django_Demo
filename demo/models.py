from django.db import models

# One to one relation
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=32, blank=False, unique=True, null=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    is_published = models.BooleanField(default=False)

    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# One to many relation
class Character(models.Model):
    name = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')

# many to many relation
class Author(models.Model):
    name = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=30, blank=True)
    books = models.ManyToManyField(Book, related_name='authors')