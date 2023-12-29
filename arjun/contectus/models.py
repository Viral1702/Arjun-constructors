from django.db import models
class Contectus(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    massage = models.TextField()
# Create your models here.
