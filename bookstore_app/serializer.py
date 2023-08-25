from rest_framework import serializers
from .models import *


class BookListSerializer(serializers.ModelSerializer):
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