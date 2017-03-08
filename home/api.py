import models
import serializers
from rest_framework import viewsets, permissions


class DeviceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Device class"""

    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoomViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class SensorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Sensor class"""

    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the DeviceType class"""

    queryset = models.DeviceType.objects.all()
    serializer_class = serializers.DeviceTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResidentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Resident class"""

    queryset = models.Resident.objects.all()
    serializer_class = serializers.ResidentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResidentStateViewSet(viewsets.ModelViewSet):
    """ViewSet for the ResidentState class"""

    queryset = models.ResidentState.objects.all()
    serializer_class = serializers.ResidentStateSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResidentActionsViewSet(viewsets.ModelViewSet):
    """ViewSet for the ResidentActions class"""

    queryset = models.ResidentActions.objects.all()
    serializer_class = serializers.ResidentActionsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResidentActionTypesViewSet(viewsets.ModelViewSet):
    """ViewSet for the ResidentActionTypes class"""

    queryset = models.ResidentActionTypes.objects.all()
    serializer_class = serializers.ResidentActionTypesSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResidentResponseViewSet(viewsets.ModelViewSet):
    """ViewSet for the ResidentResponse class"""

    queryset = models.ResidentResponse.objects.all()
    serializer_class = serializers.ResidentResponseSerializer
    permission_classes = [permissions.IsAuthenticated]


class SensorValueViewSet(viewsets.ModelViewSet):
    """ViewSet for the SensorValue class"""

    queryset = models.SensorValue.objects.all()
    serializer_class = serializers.SensorValueSerializer
    permission_classes = [permissions.IsAuthenticated]


class SensorTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the SensorType class"""

    queryset = models.SensorType.objects.all()
    serializer_class = serializers.SensorTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceTimeViewSet(viewsets.ModelViewSet):
    """ViewSet for the DeviceTime class"""

    queryset = models.DeviceTime.objects.all()
    serializer_class = serializers.DeviceTimeSerializer
    permission_classes = [permissions.IsAuthenticated]


