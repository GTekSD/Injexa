from django.db import models

class Policy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    pattern = models.CharField(max_length=255)

class Log(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    url = models.CharField(max_length=255)
    headers = models.TextField()
    data = models.TextField()
    result = models.TextField()
