from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publish_date=models.DateField()

    def __str__(self):
        return  self.title

class Author(models.Model):
    authors=models.CharField(max_length=200)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.authors

class Student(models.Model):
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=100)
    course=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"