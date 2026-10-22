from rest_framework import generics
from .models import Janr, Book
from .serializers import JanrSerializer, BookSerializer


class JanrListCreateView(generics.ListCreateAPIView):
    queryset = Janr.objects.all()
    serializer_class = JanrSerializer

    def get_queryset(self):
        return Janr.objects.all()

    def get_serializer_class(self):
        return JanrSerializer


class JanrDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Janr.objects.all()
    serializer_class = JanrSerializer
    lookup_field = "id"
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        return Janr.objects.all()

    def get_serializer_class(self):
        return JanrSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.select_related("genre").all()

    def get_serializer_class(self):
        return BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        return Book.objects.select_related("genre").all()

    def get_serializer_class(self):
        return BookSerializer
