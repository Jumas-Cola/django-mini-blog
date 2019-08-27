from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Blog(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    description = models.TextField(
        max_length=10000,
        help_text='Enter a description of blog'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-created']


class Blogger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(
        max_length=10000,
        help_text='Enter a bio of blogger'
    )

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])

    class Meta:
        ordering = ['user']


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(
        max_length=10000,
        help_text='Enter comment about blog here.'
    )

    def __str__(self):
        len_title = 75
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring

    class Meta:
        ordering = ['created']
