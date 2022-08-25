from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Participant, Core, Manager, Developer


# Register your models here.

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("user", "firstName", "lastName", "email", "contact", "college")
    search_fields = ['user__username', 'user__first_name', "user__last_name"]

    def firstName(self, obj):  # function to get firstName of any user derived object
        return obj.user.first_name

    def lastName(self, obj):  # function for last name
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email

    def contact(self, obj):
        return obj.contact

    def college(self, obj):
        return obj.college


@admin.register(Core)
class CoreAdmin(admin.ModelAdmin):
    list_display = ("user", "firstName", "lastName")

    def firstName(self, obj):  # function to get firstName of any user derived object
        return obj.user.first_name

    def lastName(self, obj):  # function for last name
        return obj.user.last_name


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ("user", "firstName", "lastName")

    def firstName(self, obj):  # function to get firstName of any user derived object
        return obj.user.first_name

    def lastName(self, obj):  # function for last name
        return obj.user.last_name


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("user", "firstName", "lastName")

    def firstName(self, obj):  # function to get firstName of any user derived object
        return obj.user.first_name

    def lastName(self, obj):  # function for last name
        return obj.user.last_name
