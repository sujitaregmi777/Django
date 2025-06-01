from django.db import models
from django.contrib.auth.models import User


class Data(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class Details(models.Model):
#     name = models.CharField(max_length=100)
#     school_name = models.CharField(max_length=100)
#     class_name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15, blank=True)
#     gpa = models.CharField(max_length=5, blank=True)
#     data = models.ManyToManyField(Data, blank=True)

#     def __str__(self):
#         return self.name

class Education(models.Model):
    details = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='educations')
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)

class Experience(models.Model):
    details = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

class Skill(models.Model):
    details = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, blank=True)

