from django.contrib import admin
from .models import *


@admin.register(Bills)
class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'client_name',
        'client_org',
        'number',
        'date',
        'service',
        'bills_sum']
