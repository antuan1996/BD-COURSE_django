from django import forms
from .models import Device, Room, Sensor, DeviceType, Resident, ResidentState, ResidentActions, ResidentActionTypes, ResidentResponse, SensorValue, SensorType, DeviceTime


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'room', 'type']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'area', 'height']


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'min_value', 'max_value', 'room', 'type']


class DeviceTypeForm(forms.ModelForm):
    class Meta:
        model = DeviceType
        fields = ['value']


class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ['sex', 'age', 'user', 'state']


class ResidentStateForm(forms.ModelForm):
    class Meta:
        model = ResidentState
        fields = ['value']


class ResidentActionsForm(forms.ModelForm):
    class Meta:
        model = ResidentActions
        fields = ['time', 'type', 'resident']


class ResidentActionTypesForm(forms.ModelForm):
    class Meta:
        model = ResidentActionTypes
        fields = ['value', 'result_state']


class ResidentResponseForm(forms.ModelForm):
    class Meta:
        model = ResidentResponse
        fields = ['satisfactory', 'resident', 'sensor_value']


class SensorValueForm(forms.ModelForm):
    class Meta:
        model = SensorValue
        fields = ['time', 'value', 'sensor']


class SensorTypeForm(forms.ModelForm):
    class Meta:
        model = SensorType
        fields = ['value']


class DeviceTimeForm(forms.ModelForm):
    class Meta:
        model = DeviceTime
        fields = ['start_time', 'finish_time', 'device']


