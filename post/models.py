from django.db import models

# Create your models here.
from django.db.models import Model


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.description} - {self.date}'


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title