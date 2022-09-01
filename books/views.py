from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter


class GetAddAuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = "List Author"
    filter_backends = [SearchFilter]
    search_fields = ['name']


class getUpdateDeleteAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = "Single Author"


class GetAddBooksView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = "List Books"
    filter_backends = [SearchFilter]
    search_fields = ['name']


class GetUpdateDeleteBookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = "Single Book"
