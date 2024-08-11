from django.db import models

# Create your models here.

class TodoModel(models.Model):
    text=models.CharField(max_length=255)