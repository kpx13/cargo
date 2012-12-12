# -*- coding: utf-8 -*-
from django.db import models

from pytils import dt

CARGO_TYPES = (
    ('O', u'Обычная'),
    ('K', u'Курьерская'),
)

class Order(models.Model):
    cargo_type = models.CharField(u'Тип доставки', max_length=1, choices=CARGO_TYPES)
    start_point = models.CharField(u'Пункт отправки ', max_length=150)
    end_point = models.CharField(u'Пункт назначения', max_length=150)
    cargo_size = models.CharField(u'Вес и размеры груза', max_length=150)
    cargo_date = models.CharField(u'Даты поставки', max_length=150)
    organization = models.CharField(u'Название организации', max_length=150)
    contact = models.CharField(u'Контактное лицо', max_length=150)
    phone = models.CharField(u'Телефон', max_length=15)
    email = models.EmailField(u'Email', blank=True)
    comment = models.CharField(u'Комментарий', max_length=150, blank=True)
    order_date = models.DateTimeField(u'Дата заказа', auto_now_add=True)

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'
        ordering = ['-order_date']

    def __unicode__(self):
        return u'Заказ %s (%s) от %s' % (self.id, self.organization, dt.ru_strftime(u"%d %B %Y", self.order_date))


class QualityFeedback(models.Model):
    fio = models.CharField(u'Ф.И.О', max_length=150)
    company = models.CharField(u'Компания', max_length=150)
    phone = models.CharField(u'Телефон', max_length=150)
    email = models.EmailField(u'Email', blank=True)
    comment = models.TextField(u'Текст')
    feedback_date = models.DateTimeField(u'Дата заказа', auto_now_add=True)

    class Meta:
        verbose_name = u'Отзыв о качестве'
        verbose_name_plural = u'Отзывы о качестве'
        ordering = ['-feedback_date']

    def __unicode__(self):
        return u'Отзыв о качестве %s от %s' % (self.id, dt.ru_strftime(u"%d %B %Y", self.feedback_date))
