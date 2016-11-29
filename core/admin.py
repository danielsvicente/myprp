from django.contrib import admin
from .models import TransactionType, Category, Transaction, Dashboard

admin.site.register(Transaction)
admin.site.register(TransactionType)
admin.site.register(Category)
admin.site.register(Dashboard)
