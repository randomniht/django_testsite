from django.db import models

# Create your models here.

class Promt(models.Model):
    name = models.CharField(max_length=250, verbose_name='promt_name')
    text = models.TextField(max_length=250, verbose_name='text')
    created_at = models.DateTimeField(auto_now=True, verbose_name='date')
    
    class Meta:
        verbose_name = 'Promt'
        verbose_name_plural = 'Promts'
    def __str__(self):
        
        return self.name