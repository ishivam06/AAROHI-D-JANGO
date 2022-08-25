from django.contrib import admin
from .models import Payment, Dispute
# Register your models here.

@admin.register(Dispute)
class DisputeAdmin(admin.ModelAdmin): 

    list_display = ("payment", "event", "description", "resolved")
    list_filter = ("event","resolved")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin): 

    list_display = ("payment_id", "event", "email", "contact", "amount")
    list_filter = ("event",)

