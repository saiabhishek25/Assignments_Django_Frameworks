from rest_framework import serializers
from .models import Book, Author,Student

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','title','author','publish_date']
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['id','authors','username','password']
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','age','course']

    def validate_age(self, value):
        try:
            val = int(value)
            if val <= 5:
                raise serializers.ValidationError("Age must be greater than 5")
        except ValueError:
            raise serializers.ValidationError("Age must be a valid number")
        return value
        