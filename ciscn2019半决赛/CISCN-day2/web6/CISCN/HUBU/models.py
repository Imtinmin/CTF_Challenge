from django.db import models

class paper(models.Model):
    key = models.CharField(max_length=10)
    content = models.TextField()
    