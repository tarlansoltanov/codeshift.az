from django.contrib import admin

from server.apps.base.models import Contact, Message


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "address", "instagram", "facebook")

    def has_add_permission(self, request):
        return not self.model.objects.exists()


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "subject", "date")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
