from django.db import models

class Book (models.Model):
     title = models.CharField(max_length=32, blank=False, unique=True, null=True)
     description = models.TextField(max_length=256, blank=True)
     price = models.DecimalField(max_digits=16, decimal_places=2, default=0)
     is_published = models.BooleanField(default=False)
