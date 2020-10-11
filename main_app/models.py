from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class MyActivity(models.Model):
    name = models.CharField(max_length=250)
    savings = models.IntegerField()
    about = models.CharField(max_length=250)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse('my_activity_detail', kwargs={'pk': self.id})


class Activity(models.Model):
    name = models.CharField(max_length=250)
    savings = models.IntegerField()
    about = models.CharField(max_length=250)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)