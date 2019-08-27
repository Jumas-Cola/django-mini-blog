from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Blog(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    description = models.TextField(
        max_length=10000,
        help_text="Enter a description of blog"
    )

    def __str__(self):
        return self.title


class Blogger(models.Model):
    pass
