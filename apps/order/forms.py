# encoding: utf-8
from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template import Context, Template
from models import Order, QualityFeedback


def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        settings.SEND_ALERT_EMAIL)


CARGO_TYPES = (
    ('O', u'Обычная'),
    ('K', u'Курьерская'),
)

class OrderForm(forms.Form):
    cargo_type = forms.ChoiceField(label = u'Тип отправки', choices = CARGO_TYPES, widget=forms.RadioSelect())
    start_point = forms.CharField(label = u'Пункт отправки', max_length=150, required = True, widget=forms.TextInput(attrs={'class':'inp1', 'size':'100'}) )
    end_point = forms.CharField(label = u'Пункт назначения', max_length=150, required = True, widget=forms.TextInput(attrs={'class':'inp1', 'size':'100'}) )
    cargo_size = forms.CharField(label = u'Вес и размеры груза', max_length=150, required = True, widget=forms.TextInput(attrs={'class':'inp1', 'size':'100'}) )
    cargo_date = forms.CharField(label = u'Даты поставки', max_length=150, required = True, widget=forms.TextInput(attrs={'class':'inp1', 'size':'100'}) )
    organization = forms.CharField(label = u'Название организации', max_length=150, required = True, widget=forms.TextInput(attrs={'class':'inp1', 'size':'100'}) )
    contact = forms.CharField(label = u'Контактное лицо', max_length=150, required = True, widget=forms.TextInput(attrs={'class':'inp1'}))
    phone = forms.CharField(label = u'Телефон', max_length=15, required = True, widget=forms.TextInput(attrs={'class':'inp1'}))
    email = forms.EmailField(label = u'Ваш e-mail', required = False, widget=forms.TextInput(attrs={'class':'inp1'}))
    comment = forms.CharField(label = u'Комментарий', max_length=150, required = False, widget=forms.Textarea(attrs={'class':'inp1'}))
    agree = forms.BooleanField(label = u'Я согласен(на) с условиями работы.', required = True)

    def save(self):
        cd = self.cleaned_data
        newOrder = Order(
            cargo_type=cd['cargo_type'],
            start_point=cd['start_point'],
            end_point=cd['end_point'],
            cargo_size=cd['cargo_size'],
            cargo_date=cd['cargo_date'],
            organization= cd['organization'],
            contact=cd['contact'],
            phone=cd['phone'],
            email=cd['email'],
            comment=cd['comment']
        )

        newOrder.save()

        subject=u'Поступил новый заказ на доставку',
	
        body_templ="""Поступил новый заказ на доставку\n
	Тип отправки - {{ o.get_cargo_type_display }}
	Пункт отправки - {{ o.start_point }}
	Пункт назначения - {{ o.end_point }}
	Вес и размеры груза - {{ o.cargo_size }}
	Даты поставки - {{ o.cargo_date }}
	Название организации - {{ o.organization }}
	Контактное лицо - {{ o.contact }}
	Телефон - {{ o.phone }}
	Емейл - {{ o.email }}
	Комментарий - {{ o.comment }}
	"""

        ctx = Context({
		'o': newOrder
	})
        body = Template(body_templ).render(ctx)
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
