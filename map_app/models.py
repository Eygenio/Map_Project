# map_app/models.py
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = CKEditor5Field('Полное описание', blank=True, config_name='default')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
    image = models.ImageField('Изображение', upload_to='places/')
    position = models.PositiveIntegerField('Позиция', default=0)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['position']

    def __str__(self):
        return f"{self.place.title} - Изображение {self.position}"
