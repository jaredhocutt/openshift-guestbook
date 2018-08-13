from django.db import models


class Guestbook(models.Model):
    message = models.CharField(
        'Message',
        max_length=250,
    )
