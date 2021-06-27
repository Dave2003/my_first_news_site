from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField('Ady', max_length=50)
    anons = models.CharField('anons', max_length=250)
    full_text = models.TextField('statya')
    date = models.DateTimeField('Wagty')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'
