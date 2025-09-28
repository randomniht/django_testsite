from django.db import models

from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField('Name', max_length=100)
    text = models.CharField('Text', max_length=100)
    date = models.DateTimeField('Date', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title