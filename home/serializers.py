import models

from rest_framework import serializers


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Device
        fields = (
            'pk', 
            'name', 
        )


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        fields = (
            'pk', 
            'name', 
            'area', 
            'height', 
        )


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sensor
        fields = (
            'pk', 
            'name', 
            'min_value', 
            'max_value', 
        )


class DeviceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DeviceType
        fields = (
            'pk', 
            'value', 
        )


class ResidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Resident
        fields = (
            'pk',
            'first_name',
            'last_name',
            'sex', 
            'age', 
        )


class ResidentStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ResidentState
        fields = (
            'pk', 
            'value', 
        )


class ResidentActionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ResidentActions
        fields = (
            'pk', 
            'time', 
        )


class ResidentActionTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ResidentActionTypes
        fields = (
            'pk', 
            'value', 
        )


class ResidentResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ResidentResponse
        fields = (
            'pk', 
            'satisfactory', 
        )


class SensorValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SensorValue
        fields = (
            'pk', 
            'time', 
            'value', 
        )


class SensorTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SensorType
        fields = (
            'pk', 
            'value', 
        )


class DeviceTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DeviceTime
        fields = (
            'pk', 
            'start_time', 
            'finish_time', 
        )


