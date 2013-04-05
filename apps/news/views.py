# -*- coding: utf-8 -*-

import models
    
def get_news():
    return [ {'id': a.id,
              'name': a.name,
              'date': a.date,
              'text': a.text
              } for a in models.Article.objects.filter(show=True).order_by('-date')]
    
def get_item(n_id):
    item = models.Article.objects.filter(show=True, id=n_id)[0]
    return (item.name, item.text)   