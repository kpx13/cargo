# -*- coding: utf-8 -*-
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=300, verbose_name=u'заголовок')
    header_photo = models.FileField(upload_to= 'uploads/headers', max_length=256, blank=True, verbose_name=u'шапка')
    header_photo_min = models.FileField(upload_to= 'uploads/mini_headers', max_length=256, blank=True, verbose_name=u'шапка меньше размером')
    image = models.FileField(upload_to= 'uploads/photos', max_length=256, blank=True, verbose_name=u'фотография')
    rules = models.TextField(blank=True, verbose_name=u'правила')
    show = models.BooleanField(blank=True, default=True, verbose_name=u'показывать на сайте?')
    sort_parameter = models.IntegerField(blank=True, default=0, verbose_name=u'параметр для сортировки')
    class Meta:
        verbose_name = u'элемент'
        verbose_name_plural = u'элементы'
        
    def __unicode__(self):
        return self.name
    
class Tariff(models.Model):
    from_place = models.CharField(max_length=300, verbose_name=u'от')
    to_place = models.CharField(max_length=300, verbose_name=u'до')
    from_place = models.CharField(max_length=300, verbose_name=u'стоимость')
    what = models.ForeignKey(Item, verbose_name=u'какая услуга')
    class Meta:
        verbose_name = u'тариф'
        verbose_name_plural = u'тарифы'
        
    def __unicode__(self):
        return self.name