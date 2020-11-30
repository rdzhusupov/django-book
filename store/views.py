from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.serializer import BooksSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
