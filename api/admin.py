from django.contrib import admin
from .models import *


@admin.register(Bills)
class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'client',
        'client_org',
        'number',
        'date',
        'service',
        'bills_sum']

@admin.register(Clients)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['client_name',]