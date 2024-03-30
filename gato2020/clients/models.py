# gato2020/clients/models.py
from django.db import models

class ImportantClient(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clients/images/')

    def __str__(self):
        return self.name
