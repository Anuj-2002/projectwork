from django.contrib import admin

from scan.models import Mail

# Register your models here.
class MailAdmin(admin.ModelAdmin):
    list_display = ['full_names',"time", "message"]
admin.site.register(Mail, MailAdmin)

# admin.site.register(NeedOrHelp)
