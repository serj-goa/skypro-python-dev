from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=60)
    author = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=100, decimal_places=False)
    description = models.TextField(max_length=2000, blank=True)
    address = models.CharField(max_length=60)
    is_published = models.BooleanField()

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
