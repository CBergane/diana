from django.db import models
from cloudinary.models import CloudinaryField

class Biography(models.Model):
    content = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return "Biography"

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image')
    date = models.DateField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.client_name

class ClientPartner(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Optional description
    image = CloudinaryField('image')

    def __str__(self):
        return self.name
