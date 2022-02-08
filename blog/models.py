from typing import ContextManager
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.


class Blog(models.Model):
    TYPES = (
        ('Suche', 'Suche'),
        ('Biete', 'Biete')
    )
    PRODUCTTYPES = (
        ('Produkt', 'Produkt'),
        ('Dienstleistung', 'Dienstleistung')
    )
    title = models.CharField(max_length=250)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=CASCADE)
    type = models.CharField(max_length=6, choices=TYPES, default="Suche")
    producttype = models.CharField(max_length=15, choices= PRODUCTTYPES, default="Produkt")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={'pk': self.pk})

class Images(models.Model):
    blog = models.ForeignKey(Blog, default=None, on_delete=CASCADE)
    image = models.ImageField(upload_to='blogpictures',
                              null=True,blank=True)
