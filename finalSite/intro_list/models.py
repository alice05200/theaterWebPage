from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phonenumber = models.CharField(max_length=20)
    content = models.TextField(default='無')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-timestamp"]
