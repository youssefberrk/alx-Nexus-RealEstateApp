from django.contrib import admin
from .models import (
    Lease, Application, Payment
)


@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('property', 'tenant', 'start_date', 'end_date', 'rent')
    list_filter = ('start_date', 'end_date')
    search_fields = ('property__name', 'tenant__name')


@admin.register(Application)
class Application(admin.ModelAdmin):
    list_display = ('property', 'tenant', 'name', 'application_date', 'status')
    list_filter = ('status', 'application_date')
    search_fields = ('property__name', 'tenant__name', 'name', 'email')


@admin.register(Payment)
class Payment(admin.ModelAdmin):
    list_display = ('lease', 'amount_due', 'amount_paid', 'due_date', 'payment_date', 'payment_status')
    list_filter = ('payment_status', 'due_date', 'payment_date')
    search_fields = ('lease__property__name', 'lease__tenant__name')
