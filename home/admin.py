# coding=utf-8
from django.contrib import admin
from django import forms
from .models import Device, Room, Sensor, DeviceType, Resident, ResidentState, ResidentActions, ResidentActionTypes, ResidentResponse, SensorValue, SensorType, DeviceTime


class DeviceAdminForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceAdmin(admin.ModelAdmin):
    form = DeviceAdminForm
    search_fields = ['name']

admin.site.register(Device, DeviceAdmin)


class RoomAdminForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

    height = forms.FloatField(min_value=0.1, label='Высота стен')
    area = forms.FloatField(min_value=0.1, label='Площадь пола')


class RoomAdmin(admin.ModelAdmin):
    form = RoomAdminForm

admin.site.register(Room, RoomAdmin)


class SensorAdminForm(forms.ModelForm):

    class Meta:
        model = Sensor
        fields = '__all__'


class SensorAdmin(admin.ModelAdmin):
    form = SensorAdminForm
    list_display = ['name', 'min_value', 'max_value']

admin.site.register(Sensor, SensorAdmin)


class DeviceTypeAdminForm(forms.ModelForm):

    class Meta:
        model = DeviceType
        fields = '__all__'


class DeviceTypeAdmin(admin.ModelAdmin):
    form = DeviceTypeAdminForm
    list_display = ['value']

admin.site.register(DeviceType, DeviceTypeAdmin)


class ResidentAdminForm(forms.ModelForm):

    class Meta:
        model = Resident
        fields = ['first_name', 'age', 'sex']

    age = forms.FloatField(min_value=0.1, label='Возраст')


class ResidentAdmin(admin.ModelAdmin):
    form = ResidentAdminForm
    list_display = ['first_name', 'age', 'sex']

admin.site.register(Resident, ResidentAdmin)


class ResidentStateAdminForm(forms.ModelForm):

    class Meta:
        model = ResidentState
        fields = '__all__'


class ResidentStateAdmin(admin.ModelAdmin):
    form = ResidentStateAdminForm
    list_display = ['value']

admin.site.register(ResidentState, ResidentStateAdmin)


class ResidentActionsAdminForm(forms.ModelForm):

    class Meta:
        model = ResidentActions
        fields = '__all__'


class ResidentActionsAdmin(admin.ModelAdmin):
    form = ResidentActionsAdminForm
    list_display = ['time']

admin.site.register(ResidentActions, ResidentActionsAdmin)


class ResidentActionTypesAdminForm(forms.ModelForm):

    class Meta:
        model = ResidentActionTypes
        fields = '__all__'


class ResidentActionTypesAdmin(admin.ModelAdmin):
    form = ResidentActionTypesAdminForm
    list_display = ['value']

admin.site.register(ResidentActionTypes, ResidentActionTypesAdmin)


class ResidentResponseAdminForm(forms.ModelForm):

    class Meta:
        model = ResidentResponse
        fields = '__all__'


class ResidentResponseAdmin(admin.ModelAdmin):
    form = ResidentResponseAdminForm
    list_display = ['user_name', 'satisfactory']

    def user_name(self, obj):
        return obj.resident.first_name

    user_name.admin_order_field = 'resident'  # Allows column order sorting
    user_name.short_description = 'Житель'  # Renames column head

admin.site.register(ResidentResponse, ResidentResponseAdmin)


class SensorValueAdminForm(forms.ModelForm):

    class Meta:
        model = SensorValue
        fields = '__all__'


class SensorValueAdmin(admin.ModelAdmin):
    form = SensorValueAdminForm
    list_display = ['time', 'value', 'sensor', 'get_room']
    search_fields = ('id', 'value', 'sensor__name' ,'sensor__room__name')

    def get_room(self, obj):
        return obj.sensor.room

    get_room.admin_order_field = 'sensor'  # Allows column order sorting
    get_room.short_description = u'Комната'  # Renames column head

admin.site.register(SensorValue, SensorValueAdmin)


class SensorTypeAdminForm(forms.ModelForm):

    class Meta:
        model = SensorType
        fields = '__all__'


class SensorTypeAdmin(admin.ModelAdmin):
    form = SensorTypeAdminForm
    list_display = ['value']

admin.site.register(SensorType, SensorTypeAdmin)


class DeviceTimeAdminForm(forms.ModelForm):

    class Meta:
        model = DeviceTime
        fields = '__all__'


class DeviceTimeAdmin(admin.ModelAdmin):
    form = DeviceTimeAdminForm
    search_fields = ['id']
    list_display = ['id', 'device', 'start_time', 'finish_time']
    list_display_links = ('device', 'id')

admin.site.register(DeviceTime, DeviceTimeAdmin)


