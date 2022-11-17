from django.shortcuts import render


def index(request):
    return render(
        request,
        'app/index.html',
        {'my_text': 'Hello minimal configuration Django project', 'title': 'Name of tip'}
    )