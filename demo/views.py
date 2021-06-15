from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from demo.models import Book
from .serializers import BookSerializer, BookMiniSerializer


def first(request):
    books = Book.objects.all()
    return render(request, 'first_temp.html', {'books': books})

# "Mini Serializer"
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer # BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    # details for one instance
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)