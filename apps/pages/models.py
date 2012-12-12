# -*- coding: utf-8 -*-
from django.db import models

from ckeditor.fields import RichTextField

class Page(models.Model):
    slug = models.SlugField(verbose_name=u'название')
    title = models.CharField(max_length=200, verbose_name=u'заголовок')
    content = RichTextField(blank=True, verbose_name=u'html-содержимое')
    header_content = RichTextField(blank=True, verbose_name=u'html-содержимое head')

    class Meta:
        verbose_name = u'статическая страница'
        verbose_name_plural = u'статические страницы'

    def __unicode__(self):
        return self.slug
