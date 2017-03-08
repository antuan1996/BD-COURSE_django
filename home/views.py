from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Device, Room, Sensor, DeviceType, Resident, ResidentState, ResidentActions, ResidentActionTypes, ResidentResponse, SensorValue, SensorType, DeviceTime
from .forms import DeviceForm, RoomForm, SensorForm, DeviceTypeForm, ResidentForm, ResidentStateForm, ResidentActionsForm, ResidentActionTypesForm, ResidentResponseForm, SensorValueForm, SensorTypeForm, DeviceTimeForm


class DeviceListView(ListView):
    model = Device


class DeviceCreateView(CreateView):
    model = Device
    form_class = DeviceForm


class DeviceDetailView(DetailView):
    model = Device


class DeviceUpdateView(UpdateView):
    model = Device
    form_class = DeviceForm


class RoomListView(ListView):
    model = Room


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm


class RoomDetailView(DetailView):
    model = Room


class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm


class SensorListView(ListView):
    model = Sensor


class SensorCreateView(CreateView):
    model = Sensor
    form_class = SensorForm


class SensorDetailView(DetailView):
    model = Sensor


class SensorUpdateView(UpdateView):
    model = Sensor
    form_class = SensorForm


class DeviceTypeListView(ListView):
    model = DeviceType


class DeviceTypeCreateView(CreateView):
    model = DeviceType
    form_class = DeviceTypeForm


class DeviceTypeDetailView(DetailView):
    model = DeviceType


class DeviceTypeUpdateView(UpdateView):
    model = DeviceType
    form_class = DeviceTypeForm


class ResidentListView(ListView):
    model = Resident


class ResidentCreateView(CreateView):
    model = Resident
    form_class = ResidentForm


class ResidentDetailView(DetailView):
    model = Resident


class ResidentUpdateView(UpdateView):
    model = Resident
    form_class = ResidentForm


class ResidentStateListView(ListView):
    model = ResidentState


class ResidentStateCreateView(CreateView):
    model = ResidentState
    form_class = ResidentStateForm


class ResidentStateDetailView(DetailView):
    model = ResidentState


class ResidentStateUpdateView(UpdateView):
    model = ResidentState
    form_class = ResidentStateForm


class ResidentActionsListView(ListView):
    model = ResidentActions


class ResidentActionsCreateView(CreateView):
    model = ResidentActions
    form_class = ResidentActionsForm


class ResidentActionsDetailView(DetailView):
    model = ResidentActions


class ResidentActionsUpdateView(UpdateView):
    model = ResidentActions
    form_class = ResidentActionsForm


class ResidentActionTypesListView(ListView):
    model = ResidentActionTypes


class ResidentActionTypesCreateView(CreateView):
    model = ResidentActionTypes
    form_class = ResidentActionTypesForm


class ResidentActionTypesDetailView(DetailView):
    model = ResidentActionTypes


class ResidentActionTypesUpdateView(UpdateView):
    model = ResidentActionTypes
    form_class = ResidentActionTypesForm


class ResidentResponseListView(ListView):
    model = ResidentResponse


class ResidentResponseCreateView(CreateView):
    model = ResidentResponse
    form_class = ResidentResponseForm


class ResidentResponseDetailView(DetailView):
    model = ResidentResponse


class ResidentResponseUpdateView(UpdateView):
    model = ResidentResponse
    form_class = ResidentResponseForm


class SensorValueListView(ListView):
    model = SensorValue


class SensorValueCreateView(CreateView):
    model = SensorValue
    form_class = SensorValueForm


class SensorValueDetailView(DetailView):
    model = SensorValue


class SensorValueUpdateView(UpdateView):
    model = SensorValue
    form_class = SensorValueForm


class SensorTypeListView(ListView):
    model = SensorType


class SensorTypeCreateView(CreateView):
    model = SensorType
    form_class = SensorTypeForm


class SensorTypeDetailView(DetailView):
    model = SensorType


class SensorTypeUpdateView(UpdateView):
    model = SensorType
    form_class = SensorTypeForm


class DeviceTimeListView(ListView):
    model = DeviceTime


class DeviceTimeCreateView(CreateView):
    model = DeviceTime
    form_class = DeviceTimeForm


class DeviceTimeDetailView(DetailView):
    model = DeviceTime


class DeviceTimeUpdateView(UpdateView):
    model = DeviceTime
    form_class = DeviceTimeForm

