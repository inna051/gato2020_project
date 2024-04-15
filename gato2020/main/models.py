from django.db import models

class MainModel(models.Model):
    title = models.CharField(
        max_length=100
    ),

    text = models.TextField(),

    image = models.ImageField(
        upload_to='main_images'
    )
