from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import EventMail

def send_account_creation_mail(receiver):

    name = f"{receiver.first_name} {receiver.last_name}"

    subject = "Registration Success - Aarohi'22"
    html_message = render_to_string('account_creation_mail.html',context={"name":name, "id":receiver.username})
    plain_message = strip_tags(html_message)
    from_email = "noreplyaarohi2022@gmail.com"
    to = receiver.email

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def send_new_password_mail(receiver, password):

    name = f"{receiver.first_name} {receiver.last_name}"

    subject = "Temporary Password - Aarohi'22"
    html_message = render_to_string('new_password_mail.html',context={"name":name, "password":password})
    plain_message = strip_tags(html_message)
    from_email = "noreplyaarohi2022@gmail.com"
    to = receiver.email

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def send_event_registration_mail(receiver, event):

    mailObj = EventMail.objects.filter(event_id = event.pk)
    #check if custom mail exists

    if mailObj:

        mailObj = EventMail.objects.get(event_id = event.pk)
        mail_subject = mailObj.subject
        mail_body = mailObj.body

    #fall back
    else:

        mail_subject = f"Registration Success - {event.title}"    
        mail_body = f"You have successfully registered for {event.title}"

    name = f"{receiver.user.first_name} {receiver.user.last_name}"

    subject = mail_subject
    html_message = render_to_string('event_registration_mail.html',context={"name":name, "body":mail_body})
    plain_message = strip_tags(html_message)
    from_email = "noreplyaarohi2022@gmail.com"
    to = receiver.user.email

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)




