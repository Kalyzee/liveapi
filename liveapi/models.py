from django.db import models

class Event(models.Model):
    first_name = models.CharField(max_length=30)
