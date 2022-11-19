from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    # path('', index, name='home'),
    path('', MailingsView.as_view(), name='home'),
    path('<int:pk>', MailingView.as_view(), name='detail_mailing'),
]