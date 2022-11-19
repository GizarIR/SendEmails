from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class Mailing(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя рассылки")
    email_template = RichTextUploadingField(blank=True, default='', verbose_name="Шаблон")
    emails = models.TextField(blank=True, verbose_name="Список рассылки")

    def __str__(self):
        return f"{self.pk}, {self.name}, {self.email_template}, {self.emails}"

    def get_absolute_url(self):
        # home  - name of route
        return reverse('detail_mailing', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
