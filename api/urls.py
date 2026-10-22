from django.urls import path
from .views import BookAPIView, JanrAPIView

urlpatterns = [
    path("genres/", JanrAPIView.as_view()),
    path("genres/<int:pk>/", JanrAPIView.as_view()),

    path("books/", BookAPIView.as_view()),
    path("books/<int:pk>/", BookAPIView.as_view()),
]
