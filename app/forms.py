from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import Textarea

from .models import *

class MailingForm(forms.ModelForm):
    email_template = forms.CharField(widget=CKEditorUploadingWidget(attrs={'cols': 80, 'rows': 15}), label="Шаблон")
    emails = forms.CharField(widget=Textarea(attrs={'cols': 80, 'rows': 5}), label="Адреса")

    class Meta:
        model = Mailing
        fields = [
            'name',
            'email_template',
            'emails',
            ]

