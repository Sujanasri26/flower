from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='flowers/')

    def __str__(self):
        return self.name
