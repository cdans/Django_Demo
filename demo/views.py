from django.shortcuts import render
from rest_framework import viewsets

from demo.models import Book
from .serializers import BookSerializer


def first(request):
    books = Book.objects.all()
    return render(request, 'first_temp.html', {'books': books})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
