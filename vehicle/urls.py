from django.urls import path

from vehicle.apps import VehicleConfig
from rest_framework import routers

from vehicle.views import CarViewSet, MotoCreateAPIView, MotoListAPIView, MotoRetrieveAPIView, MotoUpdateAPIView, \
    MotoDestroyAPIView, MileageCreateAPIView, MotoMileageListAPIView, MileageListAPIView

app_name = VehicleConfig.name

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')


urlpatterns = [
    path('moto/create/', MotoCreateAPIView.as_view(), name='moto-create'),
    path('moto/', MotoListAPIView.as_view(), name='moto-list'),
    path('moto/<int:pk>/', MotoRetrieveAPIView.as_view(), name='moto-get'),
    path('moto/update/<int:pk>/', MotoUpdateAPIView.as_view(), name='moto-update'),
    path('moto/delete/<int:pk>/', MotoDestroyAPIView.as_view(), name='moto-delete'),

    # mileage
    path('mileage/create/', MileageCreateAPIView.as_view(), name='mileage-create'),
    path('mileage/moto/', MotoMileageListAPIView.as_view(), name='mileage-moto-list'),
    path('mileage/', MileageListAPIView.as_view(), name='mileage-list'),
] + router.urls



