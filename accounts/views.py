from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from .models import Participant
from django.urls import reverse

from .forms import RegistrationForm, ParticipantInfoForm, ParticipantLoginForm
from .mailing import send_userID, send_newPassword
from django.contrib import messages
from mails.mailing_helpers import send_account_creation_mail, send_new_password_mail
from events.models import Registration, Event

# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('../profile')
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        participant_info = ParticipantInfoForm(request.POST)
        if form.is_valid() and participant_info.is_valid():
            user = form.save()
            participant = participant_info.save(commit=False)
            participant.user = user
            participant.save()
            # Successful registration,send mail
            # Uncomment below ine after adding mail credentails in mailing.py
            # try:
            #send_userID(user.email, user.username)
            #
            # regis = True

            send_account_creation_mail(user)

            context = {
                'message': "Successfully registered, please check your mail for your Aarohi-ID.",
                'redirect_link': '/accounts/login',
                'redirect_text': 'Go to Login'
            }

            return render(request, 'success.html', context)
        else:
            # print("Something went wrong")
            args = {'form': form, 'participant_info': participant_info}
            return render(request, 'reg_form.html', args)


    else:
        form = RegistrationForm()
        participant_info = ParticipantInfoForm()
        args = {'form': form, 'participant_info': participant_info}
        return render(request, 'reg_form.html', args)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('../profile')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        form = ParticipantLoginForm(data=request.POST)
        user = authenticate(request, username=username, password=password)
        if form.is_valid() and user:
            # redirect to homepage , the credentials are correct
            login(request, user)
            # Get Participant data?
            args = {}
            if Participant.objects.filter(user=user):
                participant_info = Participant.objects.get(user=user)
                # args={'participant_info':participant_info}
                event_set = Registration.objects.filter(participants=participant_info)
                events_reg = []
                for reg_obj in event_set:
                    events_reg.append(reg_obj.event.title)
                args = {'participant_info': participant_info, 'events': events_reg}
            return render(request, 'profile.html', args)
        else:
            # raise incorrect credentials error
            args = {'form': form, 'message': 'Invalid Credentials'}
            return render(request, 'login_form.html', args)
    else:
        form = ParticipantLoginForm()
    return render(request, 'login_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('../login')


@login_required  # here if not logged in then user is automatically redirected to settings.LOGIN_URL
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile_view(request):
    args = {}
    if Participant.objects.filter(user=request.user):
        participant_info = Participant.objects.get(user=request.user)

        event_set = Registration.objects.filter(participants=participant_info)
        events_reg = []
        for reg_obj in event_set:
            events_reg.append(reg_obj.event.title)
        args = {'participant_info': participant_info, 'events': events_reg}
    return render(request, 'profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Revalidate the user session,with new details
            args = {}
            # as we are now redirecting to success page we dont need to events info hence commenting out below part
            # if Participant.objects.filter(user=form.user):
            #     participant_info=Participant.objects.get(user=form.user)
            #    # args={'participant_info':participant_info}
            #     event_set = Registration.objects.filter(participants=participant_info)
            #     events_reg=[]
            #     for reg_obj in event_set:
            #         events_reg.append(reg_obj.event.title)
            #     args={'participant_info':participant_info,'events':events_reg}
            args = {
                "message": "You have successfully changed your password.",
                "redirect_link": "/accounts/profile",
                "redirect_text": "Go back to your profile"
            }
            return render(request, 'success.html', args)
        else:
            # return HttpResponse("Error occured?")
            # messages.info(request,"Invalid Details entered,try again")
            return render(request, 'change_password.html', {'form': form})

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)


# Add protection of access(Not accessible if logged in and stuff)
def reset_password(request):
    # Render a basic template asking for email id and userid?
    # Get that data,and send a mail consisting of a token generated using rng?
    # Now try to verify these details
    if request.method == 'POST':
        # current_user=User.objects.filter(username=request.POST.get('userID'))
        if User.objects.filter(username=request.POST.get('userID')):
            current_user = User.objects.get(username=request.POST.get('userID'))
            # if current_user:
            # User exists
            print(current_user)
            if current_user.email == request.POST.get('email'):
                # Valid data,proceed to change password
                # print("Changing password to abcdroot")
                # For testing purpose,just see if password is being changed....
                # WHile deployment,Use RNG to generate and then mail the new password
                # password_string='abcdroot'
                password_string = get_random_string(length=8)
                print(password_string)
                current_user.password = make_password(password_string)
                current_user.save()

                send_new_password_mail(current_user, password_string)
        
                context = {
                    'message': "Successfully reset the password, please check your email.",
                    'redirect_link': '/accounts/login',
                    'redirect_text': 'Go to Login'
                }

                return render(request, "success.html", context)
            else:
                # print("Invalid details,not allowing to proceed")
                message = "Invalid details, not allowing to proceed"
                errorcode = "500"
                return render(request, "error.html", {'message': message, 'errorcode': errorcode})
        else:
            message = "No such user exists."
            errorcode = "404"
            return render(request, "error.html", {'message': message, 'errorcode': errorcode})

    else:
        return render(request, 'reset_pass_form.html')


# these views are just to test frontned of error and success pages

def success_page(request):
    return render(request, 'success.html')


def error_page(request):
    return render(request, 'error.html')