from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    reg_date = models.DateTimeField('registration date')
    picture = models.ImageField(upload_to='avatars', height_field=50, width_field=50)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.DateTimeField('publication date')
    redact_date = models.DateTimeField('last modified date')
    picture = models.ImageField(upload_to='postImage', height_field=100, width_field=100)


class Tag(models.Model):
    tag = models.CharField(max_length=20)
    post = models.ManyToManyField(Post)