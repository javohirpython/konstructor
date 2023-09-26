from django.db import models

# Create your models here.


class Libraries(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone_num = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    leader = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name