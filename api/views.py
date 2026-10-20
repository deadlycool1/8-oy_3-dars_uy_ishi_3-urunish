from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.forms import model_to_dict
from .models import Janr, Book

class BookAPIView(APIView):
    def get(self, request: Request):
        books = Book.objects.all()
        books_list = []
        for book in books:
            books_list.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "pages": book.pages,
                    "janr": book.genre.id
                }
            )
        return Response(books_list)

    def post(self, request):
        book = Book.objects.create(**request.data)
        return Response(model_to_dict(book))

class JanrAPIView(APIView):
    def get(self, request: Request):
        janrlar = Janr.objects.all()
        janrlar_list = []
        for janr in janrlar:
            janrlar_list.append(
                {
                    "id": janr.id,
                    "name": janr.name
                }
            )
        return Response(janrlar_list)
    def post(self, request):
        janr = Janr.objects.create(**request.data)
        return Response(model_to_dict(janr))