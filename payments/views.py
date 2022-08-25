from dis import dis
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from events.models import Event, Registration
from accounts.models import Participant
from .models import Payment, Dispute
from mails.mailing_helpers import send_event_registration_mail
# Create your views here.

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def payload(request):

    data = request.data
    payload_data = data["payload"]
    payment_data = payload_data["payment"]["entity"]
    payment_id = payment_data["id"]
    payment_amount = payment_data["amount"]/100  # convert to rupees
    payment_email = payment_data["email"]
    payment_contact = payment_data["contact"]
    payment_notes = payment_data["notes"]
    event_name = payment_notes["event"]

    # get event from event name
    # case insensitive matching
    event = Event.objects.get(title__iexact = event_name)

    #assume event definately exists - correct event name in form select box

    #create a payment object for that event
    payment = Payment.objects.create(payment_id = payment_id, 
                                    email= payment_email, 
                                    contact = payment_contact, 
                                    amount = payment_amount,
                                    event= event)

    #extract aarohi ids from notes
    non_id_keys = ["event","phone","email"]

    participant_ids = []

    for key, val in payment_notes.items():

        if key not in non_id_keys:

            participant_ids.append(val)


    participants = []
    DISPUTE = 0
    invalid_ids = []

    for pid in participant_ids: 
        
        #uppercase and then match
        pid = pid.upper()
        participant = Participant.objects.filter(user__username = pid)

        #check if id exists
        if participant:
            participant = Participant.objects.get(user__username = pid)
            participants.append(participant)
        else:
            #id does not exist .. make entry in dispute table
            DISPUTE = 1
            invalid_ids.append(pid)

    #create a dispute table entry
    if DISPUTE:

        invalid_ids_str = ",".join(invalid_ids)
        Dispute.objects.create(payment= payment, 
                            event= event, 
                            description= f"Invalid id - {invalid_ids_str}")

    
    #if there is no dispute make registration
    else:

        registration = Registration(event=event, num_participants= len(participants))
        #create id key 
        registration.save()
        #add participants
        for participant in participants:
            registration.participants.add(participant)
            #send mail
            send_event_registration_mail(participant, event)
            
        registration.save()
    
    return Response(request.data, status=status.HTTP_201_CREATED)
