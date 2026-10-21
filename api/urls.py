from django.urls import path
from .views import BookAPIView, JanrAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view()),
    path('janrlar/', JanrAPIView.as_view()),
]