from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address', 'instagram', 'facebook')

    def has_add_permission(self, request):
        return not self.model.objects.exists()