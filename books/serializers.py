from rest_framework import serializers
from .models import Author,Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=('pk','name','address','gender','age')

class BookSerializer(serializers.ModelSerializer):
    image=serializers.FileField()
    class Meta:
        model=Book
        fields=('pk','name','author','publishDate','NoOfPages','image')
