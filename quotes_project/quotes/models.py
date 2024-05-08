from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Add additional quote fields here (optional)
    # e.g., tags, categories

    def __str__(self):
        return f"{self.text} - {self.author}"
