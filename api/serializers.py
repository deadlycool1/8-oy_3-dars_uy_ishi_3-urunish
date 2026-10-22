from rest_framework import serializers
from .models import Janr, Book


class JanrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janr
        fields = "__all__"
        depth = 0
        read_only_fields = ["id"]
        extra_kwargs = {
            "name": {"required": True}
        }


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = []
        depth = 1
        read_only_fields = ["id"]
        extra_kwargs = {
            "title": {"required": True},
            "author": {"required": True}
        }
