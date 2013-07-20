# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
admin.autodiscover()

import settings
import views

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'^$', views.home_page),
    url(r'^lk$', views.lk_page),
    url(r'^rates/(?P<page_id>\w+)$',    views.rates_page,   name='rates_page'),
    url(r'^page$' , 'views.page'),
    url(r'^page/(?P<page_name>\w+)$' , views.get_page,     name='static_page'),
    url(r'^order$',                     views.order_page,   name='order_page'),
    url(r'^feedback$',                  views.feedback_page,name='feedback_page'),
    url(r'^calc$',                     views.calc_page,   name='calc_page'),
    url(r'^news/(?P<n_id>\w+)$',        views.news_page,    name='news_page'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
)
