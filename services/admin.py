from django.contrib import admin
from .models import Service, Category


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated','wallet_donate','amount_donate', 'amount_needed', 'progress', 'completed')

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)