from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default=False)
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title
