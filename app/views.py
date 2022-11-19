import smtplib

from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.mail import EmailMultiAlternatives


from .models import *
from .forms import *

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def index(request):
    return render(
        request,
        'app/index.html',
        {'my_text': 'Hello minimal configuration Django project', 'title': 'Name of tip'}
    )

class MailingsView(ListView):
    model = Mailing
    template_name = 'app/list_mailings.html'
    context_object_name = 'mailings'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Список рассылок'
        return context


class MailingView(DetailView):
    model = Mailing

class MailingUpdateView(UpdateView):
    form_class = MailingForm
    model = Mailing
    template_name = 'app/mailing_update.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактирование"
        return context


class MailingAddView(CreateView):
    form_class = MailingForm
    model = Mailing
    template_name = 'app/mailing_update.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Добавление рассылки"
        return context


def send_mailing(request, pk_mailing):
    mailing = Mailing.objects.get(pk=pk_mailing)
    mailing_list = mailing.emails.split(" ")
    print(f'Список рассылки готов к отправке: {mailing_list}')
    for email in mailing_list:
        # здесь можно использовать Celery для асинхронной рассылки
        msg = EmailMultiAlternatives(
            subject=mailing.name,
            body='',
            from_email='admin@admin.ru',
            to=[email],
        )
        msg.attach_alternative(mailing.email_template, "text/html")

        print(f'Отправка письма подписчику {email}...')
        try:
            msg.send()
        except smtplib.SMTPRecipientsRefused:
            print(f'Error: Ошибка отправки письма по адресу: {email}')
    return render(
        request,
        'app/index.html',
        {'my_text': f'Рассылка: {mailing.name} отправлена', 'title': 'Статус рассылки'}
    )
