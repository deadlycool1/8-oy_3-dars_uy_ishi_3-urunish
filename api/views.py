
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Janr, Book
from .serializers import JanrSerializer, BookSerializer


class JanrAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            janr = get_object_or_404(Janr, pk=pk)
            serializer = JanrSerializer(janr)
            return Response(serializer.data)

        janrlar = Janr.objects.all()
        serializer = JanrSerializer(janrlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JanrSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        janr = get_object_or_404(Janr, pk=pk)
        serializer = JanrSerializer(janr, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        janr = get_object_or_404(Janr, pk=pk)
        janr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            book = get_object_or_404(Book, pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
