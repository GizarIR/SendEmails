from django.http import HttpResponseNotFound
from django.shortcuts import render


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def index(request):
    return render(
        request,
        'app/index.html',
        {'my_text': 'Hello minimal configuration Django project', 'title': 'Name of tip'}
    )