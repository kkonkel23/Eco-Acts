from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.
# class MyActivity(models.Model):
#     name = models.CharField(max_length=250)
#     savings = models.IntegerField()
#     about = models.CharField(max_length=250)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse('my_activity_detail', kwargs={'pk': self.id})


class Activity(models.Model):
    name = models.CharField(max_length=250)
    savings = models.IntegerField()
    about = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'activity_id': self.id})

class MyActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_activities = models.ManyToManyField(Activity)

class Note(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_activities', kwargs={'user_id': self.id})

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    post_date = date.today()
    post = models.CharField(max_length=1000)
    posted_by = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail', kwargs={'blogpost_id': self.id})
