from multiprocessing import Manager
from rest_framework import serializers
from .models import Event
from accounts.models import Manager
from accounts.serializers import ManagerSerializer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title','description', 'image']

class EventDetailsSerializer(serializers.ModelSerializer):

    managers = ManagerSerializer(read_only=True, many=True)
    manager_id = serializers.PrimaryKeyRelatedField(queryset = Manager.objects.all(), source='managers', write_only=True, many=True) 
    
    class Meta:
        model = Event
        fields = "__all__"