from rest_framework import serializers
from .models import *


class BookListSerializer(serializers.ModelSerializer):
    # List book
    class Meta:
        model = Books
        fields = (
            'name',
            'code',
            'price',
            'description',
            'auhtor',
            'category',
      )
        
        
class CommetCreateSerializer(serializers.ModelSerializer):
    # adding a comment
    class Meta:
        model = Reviews
        fields = '__all__'
        
        
class CommentSerilizer(serializers.ModelSerializer):
    # output comment
    class Meta:
        model = Reviews
        fields = ('name', 'text', 'parent')
        
        
class BookDetailSerilizer(serializers.ModelSerializer):
    # full descriptions book
    reviews = CommetCreateSerializer(many=True)
    
    class Meta:
        model = Books
        exclude = ('draft', )