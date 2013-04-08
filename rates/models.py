# -*- coding: utf-8 -*-
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=300, verbose_name=u'заголовок')
    rules = models.TextField(blank=True, verbose_name=u'правила')
    show = models.BooleanField(blank=True, default=True, verbose_name=u'показывать на сайте?')
    sort_parameter = models.IntegerField(blank=True, default=0, verbose_name=u'параметр для сортировки')
    class Meta:
        verbose_name = u'элемент'
        verbose_name_plural = u'элементы'
        
    def __unicode__(self):
        return self.name