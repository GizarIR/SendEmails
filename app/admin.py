from django.contrib import admin


from .models import *

class MailingAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email_template',
        'emails',
    ]


admin.site.register(Mailing, MailingAdmin)

