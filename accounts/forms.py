from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Participant
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email Already Exists")
        return email

    class Meta:
        model = User
        fields = {
            # 'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        }  # All fields present in the form

    def save(self, commit=True):
        # Put the username generation logic here and set the user's field before save()
        user = super(RegistrationForm, self).save(commit=False)  # Some extra fields are remaining,hence dont commit yet
        # userID=Participant.objects.all().count()
        latestPK = Participant.objects.order_by('pk').last()
        if latestPK:
            # print(latestPK.pk)
            userID = latestPK.pk
        else:
            # First user
            userID = 0
        # Lets say the max no.of participants is 4 digit,thus logic to make 1 as 0001
        length_of_id = len(str(userID))
        if (length_of_id >= 4):
            # Error,increase max size,or handle temporarily as AAR2022_11111 and others remain as AAR2022_1111
            user.username = "AAR2022_" + str(userID)
        else:
            username = "AAR2022_"
            while (length_of_id < 4):
                username = username + '0'
                length_of_id = length_of_id + 1
            username = username + str(userID)
            user.username = username

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class ParticipantInfoForm(forms.ModelForm):
    college = forms.CharField(required=True)
    contact = forms.CharField(required=True)

    class Meta:
        model = Participant
        fields = [
            'college',
            'contact'
        ]

    def clean(self):
        super(ParticipantInfoForm, self).clean()
        contact = self.cleaned_data['contact']
        if len(contact) != 10:
            self.add_error('contact', 'Enter a valid 10 digit contact')
        elif contact.isdigit() == False:
            self.add_error('contact', 'Enter a valid contact,numbers only')


class ParticipantLoginForm(forms.Form):
    username = forms.CharField(label="Your username", max_length=15, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label="Your password", max_length=15, required=True)