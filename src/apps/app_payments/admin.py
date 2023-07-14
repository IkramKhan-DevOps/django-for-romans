from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created', 'variant', 'status', 'total')
    list_filter = ('created', 'variant', 'status')
    search_fields = ('pk',)
    readonly_fields = ('created', 'modified')


admin.site.register(Payment, PaymentAdmin)
