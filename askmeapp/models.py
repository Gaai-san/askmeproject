from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class AskmeModel(models.Model):
    title = models.CharField(max_length=100)
    datecreated = models.DateTimeField(default=timezone.now)
    detail = models.TextField(blank=True)
    urgent = models.BooleanField(default=False)
    answer = models.TextField(blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title