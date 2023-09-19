from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

class Biography(models.Model):
    content = RichTextField()
    image = CloudinaryField('image')

    def __str__(self):
        return "Biography"

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(default="Default description")
    image = CloudinaryField('image')

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(default="Default description")
    image = CloudinaryField('image')
    date = models.DateField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)
    description = RichTextField(default="Default description")
    date = models.DateField()

    def __str__(self):
        return self.client_name

class ClientPartner(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(default="Default description")
    image = CloudinaryField('image')

    def __str__(self):
        return self.name
    