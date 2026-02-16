from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Book, Author, Student, Contact
from .serializers import BookSerializer, AuthorSerializer, StudentSerializer
from django.core.mail import send_mail
from .forms import RegisterForm, ContactForm
from django.conf import settings

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Send welcome email
            send_mail(
                'Welcome to Our Platform',
                'Hello, your registration is successful.',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
            return render(request, 'app/register.html', {'form': RegisterForm(), 'success': 'Registration successful! Check your console for the email.'})
    else:
        form = RegisterForm()
    return render(request, 'app/register.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send email to admin
            send_mail(
                f'New Contact Query from {contact.name}',
                contact.message,
                contact.email, # From user
                ['admin@example.com'], # To admin
                fail_silently=False,
            )
            return render(request, 'app/contact.html', {'form': ContactForm(), 'success': 'Message sent successfully!'})
    else:
        form = ContactForm()
    return render(request, 'app/contact.html', {'form': form})