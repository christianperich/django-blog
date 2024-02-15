from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='')
    date_posted = models.TimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.author}'
    



