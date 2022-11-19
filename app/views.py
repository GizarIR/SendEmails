from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView


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

