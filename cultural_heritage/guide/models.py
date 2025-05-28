from django.db import models

class Guide(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    languages = models.CharField(max_length=200)
    image = models.ImageField(upload_to='guides/', null=True, blank=True)

    def __str__(self):
        return self.name
