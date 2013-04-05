# -*- coding: utf-8 -*-

REGISTRATION_ALERT_TO = 'annkpx@gmail.com'

from django.contrib import messages
from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render_to_response
import datetime

import pages.views
import rates.views
import news.views

from order.forms import OrderForm, FeedbackForm, FeedbackMForm

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['news'] = news.views.get_news()
    c.update(pages.views.get_common_content())
    c.update(csrf(request))
    
    if request.POST:
        form = FeedbackMForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedbackMForm()
            messages.success(request, u'Ваш отзыв успешно отправлен.')
            
    else:
        form = FeedbackMForm()

    c['feedback_form'] = form
    
    return c

def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['rates'] = rates.views.get_rates()
    c.update(pages.views.get_page('home'))
    
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def rates_page(request, page_id):
    c = get_common_context(request)
    c.update(rates.views.get_page(page_id))
    return render_to_response('rates.html', c, context_instance=RequestContext(request))

def get_page(request, page_name):
    c = get_common_context(request)
    page = pages.views.get_page(page_name)
    if page:
        c.update(page)
        c['title'] = c['title']
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    else:
        raise Http404

def page(request):
    c = get_common_context(request)
    return render_to_response('page.html', c, context_instance=RequestContext(request))

def order_page(request):
    c = get_common_context(request)
    c.update(pages.views.get_page('order'))

    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            form = OrderForm()
            c['done'] = True
            messages.success(request, u'Ваш заказ успешно отправлен.')
    else:
        form = OrderForm()

    c['form'] = form

    return render_to_response('vn.html', c, context_instance=RequestContext(request))

def feedback_page(request):
    c = get_common_context(request)
    c.update(pages.views.get_page('feedback'))

    if request.POST:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedbackForm()
            messages.success(request, u'Ваш отзыв успешно отправлен.')
    else:
        form = FeedbackForm()

    c['form'] = form

    return render_to_response('feedback.html', c, context_instance=RequestContext(request))

def news_page(request, n_id):
    c = get_common_context(request)
    try:
        c['title'], c['content'] = news.views.get_item(int(n_id))
    except:
        raise Http404
    return render_to_response('page.html', c, context_instance=RequestContext(request))

def static_page(request, pageName):
    c = get_common_context(request)
    c.update(pages.views.get_page(pageName))
    return render_to_response('page.html', c, context_instance=RequestContext(request))
