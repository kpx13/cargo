# -*- coding: utf-8 -*-
from django.db import models

from pytils import dt

CARGO_TYPES = (
    ('O', u'Обычная'),
    ('K', u'Курьерская'),
)


class Order(models.Model):
    sender_country = models.CharField(u'Страна', blank=True, max_length=255)
    sender_city = models.CharField(u'Город', blank=True, max_length=255)
    sender_postal_code = models.CharField(u'Индекс', blank=True, max_length=255)
    sender_company = models.CharField(u'Наименование Компании', blank=True, max_length=255)
    sender_address = models.CharField(u'Адрес', blank=True, max_length=255)
    sender_phone = models.CharField(u'Контактный телефон', blank=True, max_length=255)
    sender_name = models.CharField(u'ФИО отправителя', blank=True, max_length=255)
    info_pieces = models.CharField(u'Кол-во мест', blank=True, max_length=255)
    info_weight = models.CharField(u'Фактический вес', blank=True, max_length=255)
    info_density = models.CharField(u'Объемный вес', blank=True, max_length=255)
    info_dim = models.CharField(u'Габариты (ДхШхВ), см', blank=True, max_length=255)
    info_desc = models.CharField(u'Описание вложения', blank=True, max_length=255)
    info_envelope = models.BooleanField(u'Конверт', blank=True)
    info_package = models.BooleanField(u'Пакет', blank=True)
    info_box = models.BooleanField(u'Коробка', blank=True)
    info_bag = models.BooleanField(u'Мешок', blank=True)
    info_dang = models.BooleanField(u'Опасный груз', blank=True)
    remark = models.TextField(u'Примечание', blank=True)
    receiver_country = models.CharField(u'Страна', blank=True, max_length=255)
    receiver_city = models.CharField(u'Город', blank=True, max_length=255)
    receiver_postal_code = models.CharField(u'Индекс', blank=True, max_length=255)
    receiver_company = models.CharField(u'Наименование Компании', blank=True, max_length=255)
    receiver_address = models.CharField(u'Адрес *', max_length=255)
    receiver_phone = models.CharField(u'Контактный телефон *', max_length=255)
    receiver_name = models.CharField(u'ФИО получателя *', max_length=255)
    delivery_recipient = models.CharField(u'Получатель', blank=True, max_length=255)
    delivery_sender = models.CharField(u'Отправитель', blank=True, max_length=255)
    delivery_3rd = models.CharField(u'3я Сторона', blank=True, max_length=255)
    delivery_acc = models.CharField(u'№ счета', blank=True, max_length=255)
    delivery_cash = models.CharField(u'наличный расчет', blank=True, max_length=255)
    delivery_tariff = models.CharField(u'тариф', blank=True, max_length=255)
    delivery_insurance = models.CharField(u'страховой взнос', blank=True, max_length=255)
    delivery_deposit = models.CharField(u'наложенный платеж', blank=True, max_length=255)
    delivery_declared = models.CharField(u'объявленная стоимость', blank=True, max_length=255)
    delivery_total = models.CharField(u'итого', blank=True, max_length=255)
    delivery_econom = models.BooleanField(u'эконом', blank=True)
    delivery_standart = models.BooleanField(u'стандарт', blank=True)
    delivery_express = models.BooleanField(u'экспресс', blank=True)
    delivery_reserv = models.BooleanField(u'предварительный звонок', blank=True)
    delivery_hand = models.BooleanField(u'лично в руки', blank=True)
    delivery_pickup = models.BooleanField(u'самовывоз', blank=True)
    order_date = models.DateTimeField(u'Дата заказа', auto_now_add=True)
                    
    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'
        ordering = ['-order_date']

    def __unicode__(self):
        return u'Заказ %s от %s' % (self.id, dt.ru_strftime(u"%d %B %Y", self.order_date))


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

class Feedback(models.Model):
    fio = models.CharField(u'Имя', max_length=150)
    city = models.CharField(u'Город', max_length=150, blank=True)
    phone = models.CharField(u'Телефон', max_length=150, blank=True)
    email = models.EmailField(u'Email', blank=True)
    comment = models.TextField(u'Текст')
    feedback_date = models.DateTimeField(u'Дата', auto_now_add=True)

    class Meta:
        verbose_name = u'feedback'
        verbose_name_plural = u'feedback'
        ordering = ['-feedback_date']

    def __unicode__(self):
        return u'feedback %s от %s' % (self.id, dt.ru_strftime(u"%d %B %Y", self.feedback_date))
    
    def save(self, *args, **kwargs):
        super(Feedback, self).save(*args, **kwargs)
        
        from forms import sendmail
        from django.template import Context, Template
        
        subject=u'Поступила новая заявка с сайта',
    
        body_templ="""Поступила новая заявка с сайта (по форме обратной связи)\n
            Контактное лицо - {{ f.fio }}
            Телефон - {{ f.phone }}
            Емейл - {{ f.email }}
            Город - {{ f.city }}
            Текст - {{ f.comment }}
            """

        ctx = Context({
            'f': self
        })
        body = Template(body_templ).render(ctx)
        sendmail(subject, body)