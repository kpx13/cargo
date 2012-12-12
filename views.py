# -*- coding: utf-8 -*-

REGISTRATION_ALERT_TO = 'annkpx@gmail.com'

from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response
import datetime

import pages.views
import rates.views
import news.views

from order.forms import OrderForm, FeedbackForm, FeedbackMForm

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c.update(pages.views.get_common_content())
    c.update(csrf(request))
    return c

def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['rates'] = rates.views.get_rates()
    c.update(pages.views.get_page('home'))
    
    if request.POST:
        form = FeedbackMForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedbackMForm()
    else:
        form = FeedbackMForm()

    c['feedback_form'] = form
    
    return render_to_response('home.html', c)

def rates_page(request, page_id):
    c = get_common_context(request)
    c.update(rates.views.get_page(page_id))
    return render_to_response('rates.html', c)

def get_page(request, page_name):
    c = get_common_context(request)
    page = pages.views.get_page(page_name)
    if page:
        c.update(page)
        c['title'] = c['title']
        return render_to_response('page.html', c)
    else:
        return HttpResponseNotFound('not found page')

def page(request):
    c = get_common_context(request)
    return render_to_response('page.html', c)

def insert_test_data(request):
    pages.views.insert_test_data()
    rates.views.insert_test_data()
    return HttpResponseRedirect('/')

def order_page(request):
    c = get_common_context(request)
    c.update(pages.views.get_page('order'))

    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            form = OrderForm()
    else:
        form = OrderForm()

    c['form'] = form

    return render_to_response('vn.html', c)

def feedback_page(request):
    c = get_common_context(request)
    c.update(pages.views.get_page('feedback'))

    if request.POST:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedbackForm()
    else:
        form = FeedbackForm()

    c['form'] = form

    return render_to_response('feedback.html', c)


def news_page(request):
    c = get_common_context(request)
    c['news'] = news.views.get_news()

    return render_to_response('news.html', c)

def static_page(request, pageName):
    c = get_common_context(request)
    c.update(pages.views.get_page(pageName))
    return render_to_response('page.html', c)
