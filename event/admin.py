from django.contrib import admin
from .models import Event, Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'event', 'status')
    list_filter = ('status', 'event')
    actions = ['approve_registration', 'reject_registration']

    def approve_registration(self, request, queryset):
        queryset.update(status='approved')
    approve_registration.short_description = "Approve selected registrations"

    def reject_registration(self, request, queryset):
        queryset.update(status='rejected')
    reject_registration.short_description = "Reject selected registrations"

admin.site.register(Event)
admin.site.register(Registration, RegistrationAdmin)

# Register your models here.
