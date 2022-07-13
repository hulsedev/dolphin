import uuid

from django.db import models


class Log(models.Model):
    def __str__(self):
        return self.machine_id

    class Meta:
        ordering = ["created"]
