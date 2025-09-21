from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Articles(models.Model):
    title = models.CharField('Name', max_length=100)
    text = models.CharField('Text', max_length=100)
    date = models.DateTimeField('Date',auto_now_add=True )
    # def __str__(self):
    #     return f'title : {Articles.title}, text {Articles.text}, date {Articles.date} '