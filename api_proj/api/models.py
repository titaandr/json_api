from django.db import models

# Create your models here.

#class Image(models.Model):
#   link = models.CharField(max_length=200)

class Post(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
#    imageLink = models.ForeignKey(Image, on_delete=models.CASCADE)