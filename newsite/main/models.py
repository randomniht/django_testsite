from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField('Name', max_length=100)
    text = models.CharField('Text', max_length=100)
    date = models.DateTimeField('Date', auto_now_add=True)
    image = models.ImageField('Image', upload_to='articles_images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField('Likes', default=0)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Articles, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Mediapost(models.Model):
    image = models.ImageField('Image', upload_to='randomedia/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)