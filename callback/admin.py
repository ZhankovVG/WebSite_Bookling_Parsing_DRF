from django.contrib import admin
from .models import *


@admin.register(CallbackRequest)
class CallbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'time_stamp')
    list_display_links = ('phone_number', )
    readonly_fields = ('phone_number', )