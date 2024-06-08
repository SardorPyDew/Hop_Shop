from django.contrib import admin

from pages.models import ContactModel, FeedbackModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at',)
    search_fields = ('name', 'email', 'subject',)
    list_filter = ('email', 'created_at',)


@admin.register(FeedbackModel)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'job', 'created_at']
    search_fields = ['full_name', 'job']
    list_filter = ['created_at', 'job']
