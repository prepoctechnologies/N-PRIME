from django.contrib import admin
from .models import ConsultationEnquiry, CallbackRequest, ContactMessage


@admin.register(ConsultationEnquiry)
class ConsultationEnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'service', 'submitted_at', 'is_read')
    list_filter = ('service', 'is_read', 'submitted_at')
    search_fields = ('full_name', 'email', 'phone', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)


@admin.register(CallbackRequest)
class CallbackRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'preferred_time', 'submitted_at', 'is_read')
    list_filter = ('is_read', 'submitted_at')
    search_fields = ('name', 'phone')
    list_editable = ('is_read',)
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at', 'is_read')
    list_filter = ('is_read', 'submitted_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)
