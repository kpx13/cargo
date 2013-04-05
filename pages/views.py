# -*- coding: utf-8 -*-

import models

def get_page(page_name):
    try:
        page = models.Page.objects.get(slug=page_name)
        return {'title': page.title,
                'content': page.content,
                'header_content': page.header_content
                }
    except:
        return None
    