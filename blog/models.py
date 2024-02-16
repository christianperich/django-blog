from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
    
class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(default='')

    def __str__(self):
        return f'{self.title} - {self.author}'
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Entry", on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Comentario de {self.author} a //{self.post}//'
    

