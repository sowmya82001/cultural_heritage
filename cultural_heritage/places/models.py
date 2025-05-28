from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='places/', null=True, blank=True)

    def __str__(self):
        return self.name
