from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField('Name', max_length=100)
    text = models.TextField('Text')
    date = models.DateTimeField('Date', auto_now_add=True)
    image = models.ImageField('Image', upload_to='articles_images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_articles', blank=True)

    def __str__(self):
        return self.title

    # Свойство для получения количества лайков
    @property
    def likes_count(self):
        return self.liked_by.count()

    # Метод для проверки, лайкал ли пользователь
    def user_has_liked(self, user):
        if not user.is_authenticated:
            return False
        return self.liked_by.filter(id=user.id).exists() 
class Comment(models.Model):
    post = models.ForeignKey(Articles, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Mediapost(models.Model):
    image = models.ImageField('Image', upload_to='randomedia/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Word(models.Model):
    text = models.CharField(max_length=100, verbose_name='Слово')
    translate = models.CharField(max_length=100, verbose_name='Перевод')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Создатель')
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

class Note(models.Model):
    word = models.ForeignKey(Word, related_name='notes', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Заметка')
    created_at = models.DateTimeField(auto_now_add=True)
