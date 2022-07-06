from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    title = models.CharField(max_length=250)
    description = models.TextField(default=False)
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title
