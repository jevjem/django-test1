from django.db import models

# Create your models here.

'''
class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
'''

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Haзвaниe')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class Bb(models.Model):
    title = models.CharField(max_length=50 , verbose_name='Toвap')
    content = models.TextField(null=True, blank=True, verbose_name='Oпиcaниe')
    price = models.FloatField(null=True ,blank=True, verbose_name= 'Цeнa')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name= 'Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
    
