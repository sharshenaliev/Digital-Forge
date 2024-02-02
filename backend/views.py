from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from backend.serializers import *
from backend.models import *


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ManagerViewSet(ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('city', 'status')
    ordering_fields = ('number', 'floor', 'square', 'date', 'price')


class StatusView(APIView):

    def get(self, request):
        choices_models = Apartment._meta.get_field('status').choices
        data = []
        for count, name in enumerate(choices_models, 1):
            data.append({'id': count,'name': name[0]})
        return Response(data)


class CityListAPIView(ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
