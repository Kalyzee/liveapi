from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)

    begin = models.DateTimeField()
    end   = models.DateTimeField()

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
