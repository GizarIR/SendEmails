from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

class Mailing(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя рассылки")
    email_template = RichTextUploadingField(blank=True, default='', verbose_name="Шаблон")
    emails = models.TextField(blank=True, verbose_name="Список рассылки")

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
