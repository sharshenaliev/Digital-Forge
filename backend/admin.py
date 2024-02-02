from django.contrib import admin
from backend.models import *

admin.site.register(Client)
admin.site.register(City)


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    readonly_fields = ('date', )


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('number', 'client', 'status', 'floor', 'square', 'date', 'price')
    readonly_fields = ('date', )
    list_filter = ('status', 'city')
    ordering = ('number', 'floor', 'square', 'date', 'price')
