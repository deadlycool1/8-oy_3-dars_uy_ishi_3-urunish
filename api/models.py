from django.db import models

class Janr(models.Model):
    name = models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pages = models.SmallIntegerField
    genre = models.ForeignKey(Janr, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
