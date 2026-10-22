from django.urls import path
from .views import (
    JanrListCreateView,
    JanrDetailView,
    BookListCreateView,
    BookDetailView,
)

urlpatterns = [
    path("genres/", JanrListCreateView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", JanrDetailView.as_view(), name="genre-detail"),

    path("books/", BookListCreateView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
