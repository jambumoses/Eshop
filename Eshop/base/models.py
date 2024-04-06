from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to = 'images/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title