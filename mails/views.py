from django.shortcuts import render
from .mailing_helpers import send_account_creation_mail
from .models import EventMail
# Create your views here

#test the mail template
def account_creation_mail_view(request):

    send_account_creation_mail("kunalmoharkar1700@gmail.com")
    return render(request, "account_creation_mail.html", context={"name":"Kartik Kshirsagar", "id":"ARR2022_0002"})

#test the mail template
def event_registration_mail_view(request):

    #send_event_registration_mail("kunalmoharkar1700@gmail.com")
    mail = EventMail.objects.get(pk=1)
    return render(request, "event_registration_mail.html", context={"name":"Kartik Kshirsagar", "body":mail.body})