from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Book, Author,Student
from .serializers import BookSerializer, AuthorSerializer,StudentSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()   
    serializer_class=AuthorSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer