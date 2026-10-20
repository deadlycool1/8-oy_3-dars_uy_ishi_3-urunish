from django.urls import path
from .views import BookAPIView, JanrAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view()),
    path('janrs', JanrAPIView.as_view()),
]