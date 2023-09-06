from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

    #You can also specify individual fields as shown below 

    # id=serializers.UUidField()
    # title=serializers.CharField()
    # number_of_pages=serializers.IntergerField()
    # published_date = serializers.DateField()
    # quantity=serializers.IntegerField()
