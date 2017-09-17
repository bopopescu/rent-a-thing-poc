from django.contrib import admin

# Register your models here.
from core.models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount_paid', 'credits_purchased', 'price_per_credit', 'is_completed', 'user', 'transaction_code')
    fields = ('id', 'amount_paid', 'credits_purchased', 'price_per_credit', 'is_completed', 'user', 'transaction_code')
    readonly_fields = ('id', 'amount_paid', 'credits_purchased', 'price_per_credit', 'is_completed', 'user', 'transaction_code')
    ordering = ('last_update', 'created')

admin.site.register(Transaction, TransactionAdmin)