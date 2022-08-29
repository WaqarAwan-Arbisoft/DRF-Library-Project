from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer
from rest_framework.parsers import MultiPartParser,FormParser

class GetAddAuthorView(ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    name="List Author"
    parser_classes=(MultiPartParser,FormParser)
    
    

class getUpdateDeleteAuthorView(RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    name="Single Author"


class GetAddBooksView(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    name="List Books"


class GetUpdateDeleteBookView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    name="Single Book"
