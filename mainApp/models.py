from ssl import create_default_context
from django.db import models

from django.contrib.auth.models import User

#Models
class userTask(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.task 

