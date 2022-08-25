from django.contrib import admin
from .models import Event, Registration

admin.site.register(Event)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("event","num_participants","individual","name","email","phone","institute","date_of_reg",)
    list_filter = ("event","num_participants")
    search_fields = ["event__title","participants__user__username"]
    def individual(self, obj):
        return ",".join([p.user.username for p in obj.participants.all()])
    
    def name(self, obj):
        return ",".join([f"{p.user.first_name} {p.user.last_name}" for p in obj.participants.all()])

    def email(self, obj):
        return ",".join([p.user.email for p in obj.participants.all()])

    def phone(self, obj):
        return ",".join([p.contact for p in obj.participants.all()])

    def institute(self, obj):
        return ",".join([p.college for p in obj.participants.all()])
    