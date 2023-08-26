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
        
        
class BookDetailSerilizer(serializers.ModelSerializer):
    # full descriptions book
    class Meta:
        model = Books
        exclude = ('draft', )