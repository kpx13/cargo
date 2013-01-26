# -*- coding: utf-8 -*-
from django.contrib import admin
import models


class OrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'order_date',)
    ordering = ('order_date', )

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'feedback_date',)
    ordering = ('feedback_date', )


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.QualityFeedback, FeedbackAdmin)
admin.site.register(models.Feedback)