from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('account_create', views.account_creation_mail_view),
    path('event_reg', views.event_registration_mail_view),
]
