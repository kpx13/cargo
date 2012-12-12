# -*- coding: utf-8 -*-
 
from django.forms import ModelForm
from models import Review
 
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'text')
