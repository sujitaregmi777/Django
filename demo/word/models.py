
from django.db import models
from django.contrib.auth.models import User

class BaseTimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(BaseTimestampModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

def _str_(self):
    return self.title

class Comment(BaseTimestampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "comments")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "author")
    content = models.TextField()

def _str_(self):
    return f"{self.post.title}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

def _str_(self):
    return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    noofstd = models.IntegerField()


def _str_(self):
    return self.name