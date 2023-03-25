from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(blank=True)
    image = models.URLField(blank=True)
    release_date = models.DateField(blank=True)
    lte_exists = models.BooleanField(blank=True)
    slug = models.SlugField(blank=True, unique=True)
