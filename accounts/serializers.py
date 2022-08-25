from rest_framework import serializers
from .models import Manager, Participant
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    
class ManagerSerializer(serializers.ModelSerializer):
    
    user  = UserSerializer(read_only=True)

    class Meta:
        model = Manager
        fields = '__all__'