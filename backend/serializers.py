from rest_framework import serializers
from backend.models import *


class CitySerializer(serializers.ModelSerializer):

     class Meta:
        model = City
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apartment
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = '__all__'
