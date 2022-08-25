# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import permissions
# from .models import Event
# from .serializers import EventSerializer, EventDetailsSerializer
#
#
# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def events_list(request):
#
#     events = Event.objects.all()
#     serializer = EventSerializer(events, many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def event_details(request,pk):
#
#     event = Event.objects.filter(pk=pk)
#     if event:
#
#         event = Event.objects.get(pk=pk)
#         serializer = EventDetailsSerializer(event)
#         return Response(serializer.data)
#
#     return Response({"msg":"Event does not exist"},status=status.HTTP_404_NOT_FOUND)
#
#


from django.shortcuts import render
from .models import Event,  Registration
from accounts.models import Participant
# from mails.mailing import sendEventMail
import datetime


# Create your views here.

def events_list(request):

    events = Event.objects.filter(publish = True)
    print(events)
    # If user/pariticipant does not exist,render normal page,link to register should redirect to login
    mode = 1  # Implies user is logged in,0 means either not logged in or not a particicipant
    events_registered_list = []
    if request.user.is_anonymous:
        mode = 0
    elif Participant.objects.filter(user=request.user):
        participant = Participant.objects.get(user=request.user)
        events_of_user = Registration.objects.filter(participants=participant)
        # events_of_user = events_of_user.filter(type="EXB")

        for reg_obj in events_of_user:
            # print(reg_obj.event.title)
            events_registered_list.append(reg_obj.event.pk)
        # print(events_registered_dict)
    else:
        mode = 0
    return render(request, "events.html",
                  {"events": events, 'events_reg': events_registered_list, 'today_date': datetime.date.today(),
                   'mode': mode})



def event_details(request, pk):
    event = Event.objects.get(pk = pk)
    mode = 1  # Implies user is logged in,0 means either not logged in or not a particicipant
    registered = False
    if request.user.is_anonymous:
        mode = 0
    elif Participant.objects.filter(user=request.user):
        participant = Participant.objects.get(user=request.user)
        events_of_user = Registration.objects.filter(participants=participant)
        events_of_user = events_of_user.filter(event=event)
        if events_of_user:
            # Already registered
            registered = True
    else:
        mode = 0
    return render(request, 'event_details.html',
                  {'event': event, 'mode': mode, 'registered': registered, 'today_date': datetime.date.today()})



# @login_required,some imports here
def register_event(request, event_pk):
    # have checks here as well
    if request.user.is_anonymous:
        return render(request, 'error.html', {'errorcode': 610, 'message': 'You need to login as participant'})
    if Participant.objects.filter(user=request.user):
        participant = Participant.objects.get(user=request.user)
        events_of_user = Registration.objects.filter(participants=participant)
        # events_of_user = events_of_user.filter(type="EXB")
        if Event.objects.filter(pk=event_pk):
            event = Event.objects.get(pk=event_pk)
            if event.fees_non_vnit != 0:  # Conservative approach
                return render(request, 'error.html',
                              {'errorcode': 619, 'message': "Error,not allowed!Register via form!!"})
            if event.last_registration_date < datetime.date.today():
                return render(request, 'error.html', {'errorcode': 100, 'message': "Registrations have closed"})
            for reg_obj in events_of_user:
                if reg_obj.event.pk == event_pk:
                    # Error,already registered
                    return render(request, 'error.html', {'errorcode': 505, 'message': "Already registered to the DB"})
            # Not actually registered,hence register
            registration = Registration(event=event, date_of_reg=datetime.datetime.now())
            registration.save()  # To make this have an id,required for many to many
            registration.participants.add(participant)
            registration.save()
            # Final save


            # sendEventMail(event, request.user)

            return render(request, 'success.html',
                          {'message': "Successfully Registered", 'redirect_link': '/accounts/profile',
                           'redirect_text': 'Dashboard'})
        else:
            return render(request, 'error.html', {'errorcode': 404, 'message': "No such event exists"})
    else:
        return render(request, 'error.html', {'errorcode': 500, 'message': 'Not a participant'})
