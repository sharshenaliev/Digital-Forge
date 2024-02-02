from django.urls import path, include
from backend.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('client', ClientViewSet, basename='petition')
router.register('manager', ManagerViewSet, basename='mypetition')
router.register('apartment', ApartmentViewSet, basename='news')

urlpatterns = [
    path('city', CityListAPIView.as_view()),
    path('status', StatusView.as_view()),
    path('', include(router.urls)),
]
