# encoding: utf-8
from django import forms
from django.forms import ModelForm
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template import Context, Template
from models import Order, QualityFeedback, Feedback


def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        settings.SEND_ALERT_EMAIL)


CARGO_TYPES = (
    ('O', u'Обычная'),
    ('K', u'Курьерская'),
)

class OrderForm(ModelForm):
    agree = forms.BooleanField(label = u'Я согласен(на) с условиями работы.', required = True)
    
    class Meta:
        model = Order
        exclude = ('order_date', )
    

    def save(self):
        order = super(OrderForm, self).save()
        subject=u'Поступил новый заказ на доставку'
        body="""Посмотреть заказ Вы можете по адресу http://cargoexpresstrans.ru/admin/order/order/%s/""" % order.id
        sendmail(subject, body)

    def agree_clean(self):
        cd = self.cleaned_data
        if not cd['agree']:
            raise forms.ValidationError(u'Для заказа вы должны согласиться с условиями')
        return cd['agree']

class FeedbackForm(forms.Form):
    fio = forms.CharField(label = u'Ф.И.О', max_length=150, required = True, widget=forms.TextInput(attrs={'class':'inp1'}) )
    company = forms.CharField(label = u'Компания', max_length=150, required = True, widget=forms.TextInput(attrs={'class':'inp1'}) )
    phone = forms.CharField(label = u'Телефон', max_length=150, required = True, widget=forms.TextInput(attrs={'class':'inp1'}) )
    email = forms.EmailField(label = u'Ваш e-mail', required = False, widget=forms.TextInput(attrs={'class':'inp1'}))
    comment = forms.CharField(label = u'Отзыв', required = True, widget=forms.Textarea(attrs={'class':'inp1'}))

    def save(self):
        cd = self.cleaned_data
        newFeedback = QualityFeedback(
            fio = cd['fio'],
            company = cd['company'],
            phone = cd['phone'],
            email = cd['email'],
            comment = cd['comment']
        )
        newFeedback.save()

        subject=u'Поступила новая оценка качества',
        body_templ=u'Поступила новая оценка качества - {{url}}'
        ctx = Context({
            'url': reverse('admin:order_qualityfeedback_change',args=(newFeedback.id,))
        })
        body = Template(body_templ).render(ctx)
        sendmail(subject,body)


class FeedbackMForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ('feedback_date', )
