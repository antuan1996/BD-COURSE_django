import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Device, Room, Sensor, DeviceType, Resident, ResidentState, ResidentActions, ResidentActionTypes, ResidentResponse, SensorValue, SensorType, DeviceTime
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_device(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "room" not in defaults:
        defaults["room"] = create_room()
    if "type" not in defaults:
        defaults["type"] = create_devicetype()
    return Device.objects.create(**defaults)


def create_room(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["area"] = "area"
    defaults["height"] = "height"
    defaults.update(**kwargs)
    return Room.objects.create(**defaults)


def create_sensor(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["min_value"] = "min_value"
    defaults["max_value"] = "max_value"
    defaults.update(**kwargs)
    if "room" not in defaults:
        defaults["room"] = create_room()
    if "type" not in defaults:
        defaults["type"] = create_sensortype()
    return Sensor.objects.create(**defaults)


def create_devicetype(**kwargs):
    defaults = {}
    defaults["value"] = "value"
    defaults.update(**kwargs)
    return DeviceType.objects.create(**defaults)


def create_resident(**kwargs):
    defaults = {}
    defaults["sex"] = "sex"
    defaults["age"] = "age"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "state" not in defaults:
        defaults["state"] = create_residentstate()
    return Resident.objects.create(**defaults)


def create_residentstate(**kwargs):
    defaults = {}
    defaults["value"] = "value"
    defaults.update(**kwargs)
    return ResidentState.objects.create(**defaults)


def create_residentactions(**kwargs):
    defaults = {}
    defaults["time"] = "time"
    defaults.update(**kwargs)
    if "type" not in defaults:
        defaults["type"] = create_residentactiontypes()
    if "resident" not in defaults:
        defaults["resident"] = create_resident()
    return ResidentActions.objects.create(**defaults)


def create_residentactiontypes(**kwargs):
    defaults = {}
    defaults["value"] = "value"
    defaults.update(**kwargs)
    if "result_state" not in defaults:
        defaults["result_state"] = create_residentstate()
    return ResidentActionTypes.objects.create(**defaults)


def create_residentresponse(**kwargs):
    defaults = {}
    defaults["satisfactory"] = "satisfactory"
    defaults.update(**kwargs)
    if "resident" not in defaults:
        defaults["resident"] = create_resident()
    if "sensor_value" not in defaults:
        defaults["sensor_value"] = create_sensorvalue()
    return ResidentResponse.objects.create(**defaults)


def create_sensorvalue(**kwargs):
    defaults = {}
    defaults["time"] = "time"
    defaults["value"] = "value"
    defaults.update(**kwargs)
    if "sensor" not in defaults:
        defaults["sensor"] = create_django_contrib_auth_models_user()
    return SensorValue.objects.create(**defaults)


def create_sensortype(**kwargs):
    defaults = {}
    defaults["value"] = "value"
    defaults.update(**kwargs)
    return SensorType.objects.create(**defaults)


def create_devicetime(**kwargs):
    defaults = {}
    defaults["start_time"] = "start_time"
    defaults["finish_time"] = "finish_time"
    defaults.update(**kwargs)
    if "device" not in defaults:
        defaults["device"] = create_device()
    return DeviceTime.objects.create(**defaults)


class DeviceViewTest(unittest.TestCase):
    '''
    Tests for Device
    '''
    def setUp(self):
        self.client = Client()

    def test_list_device(self):
        url = reverse('home_device_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_device(self):
        url = reverse('home_device_create')
        data = {
            "name": "name",
            "room": create_room().pk,
            "type": create_devicetype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_device(self):
        device = create_device()
        url = reverse('home_device_detail', args=[device.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_device(self):
        device = create_device()
        data = {
            "name": "name",
            "room": create_room().pk,
            "type": create_devicetype().pk,
        }
        url = reverse('home_device_update', args=[device.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RoomViewTest(unittest.TestCase):
    '''
    Tests for Room
    '''
    def setUp(self):
        self.client = Client()

    def test_list_room(self):
        url = reverse('home_room_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_room(self):
        url = reverse('home_room_create')
        data = {
            "name": "name",
            "area": "area",
            "height": "height",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_room(self):
        room = create_room()
        url = reverse('home_room_detail', args=[room.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_room(self):
        room = create_room()
        data = {
            "name": "name",
            "area": "area",
            "height": "height",
        }
        url = reverse('home_room_update', args=[room.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SensorViewTest(unittest.TestCase):
    '''
    Tests for Sensor
    '''
    def setUp(self):
        self.client = Client()

    def test_list_sensor(self):
        url = reverse('home_sensor_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sensor(self):
        url = reverse('home_sensor_create')
        data = {
            "name": "name",
            "min_value": "min_value",
            "max_value": "max_value",
            "room": create_room().pk,
            "type": create_sensortype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sensor(self):
        sensor = create_sensor()
        url = reverse('home_sensor_detail', args=[sensor.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sensor(self):
        sensor = create_sensor()
        data = {
            "name": "name",
            "min_value": "min_value",
            "max_value": "max_value",
            "room": create_room().pk,
            "type": create_sensortype().pk,
        }
        url = reverse('home_sensor_update', args=[sensor.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DeviceTypeViewTest(unittest.TestCase):
    '''
    Tests for DeviceType
    '''
    def setUp(self):
        self.client = Client()

    def test_list_devicetype(self):
        url = reverse('home_devicetype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_devicetype(self):
        url = reverse('home_devicetype_create')
        data = {
            "value": "value",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_devicetype(self):
        devicetype = create_devicetype()
        url = reverse('home_devicetype_detail', args=[devicetype.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_devicetype(self):
        devicetype = create_devicetype()
        data = {
            "value": "value",
        }
        url = reverse('home_devicetype_update', args=[devicetype.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ResidentViewTest(unittest.TestCase):
    '''
    Tests for Resident
    '''
    def setUp(self):
        self.client = Client()

    def test_list_resident(self):
        url = reverse('home_resident_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_resident(self):
        url = reverse('home_resident_create')
        data = {
            "sex": "sex",
            "age": "age",
            "user": create_django_contrib_auth_models_user().pk,
            "state": create_residentstate().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_resident(self):
        resident = create_resident()
        url = reverse('home_resident_detail', args=[resident.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_resident(self):
        resident = create_resident()
        data = {
            "sex": "sex",
            "age": "age",
            "user": create_django_contrib_auth_models_user().pk,
            "state": create_residentstate().pk,
        }
        url = reverse('home_resident_update', args=[resident.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ResidentStateViewTest(unittest.TestCase):
    '''
    Tests for ResidentState
    '''
    def setUp(self):
        self.client = Client()

    def test_list_residentstate(self):
        url = reverse('home_residentstate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_residentstate(self):
        url = reverse('home_residentstate_create')
        data = {
            "value": "value",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_residentstate(self):
        residentstate = create_residentstate()
        url = reverse('home_residentstate_detail', args=[residentstate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_residentstate(self):
        residentstate = create_residentstate()
        data = {
            "value": "value",
        }
        url = reverse('home_residentstate_update', args=[residentstate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ResidentActionsViewTest(unittest.TestCase):
    '''
    Tests for ResidentActions
    '''
    def setUp(self):
        self.client = Client()

    def test_list_residentactions(self):
        url = reverse('home_residentactions_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_residentactions(self):
        url = reverse('home_residentactions_create')
        data = {
            "time": "time",
            "type": create_residentactiontypes().pk,
            "resident": create_resident().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_residentactions(self):
        residentactions = create_residentactions()
        url = reverse('home_residentactions_detail', args=[residentactions.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_residentactions(self):
        residentactions = create_residentactions()
        data = {
            "time": "time",
            "type": create_residentactiontypes().pk,
            "resident": create_resident().pk,
        }
        url = reverse('home_residentactions_update', args=[residentactions.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ResidentActionTypesViewTest(unittest.TestCase):
    '''
    Tests for ResidentActionTypes
    '''
    def setUp(self):
        self.client = Client()

    def test_list_residentactiontypes(self):
        url = reverse('home_residentactiontypes_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_residentactiontypes(self):
        url = reverse('home_residentactiontypes_create')
        data = {
            "value": "value",
            "result_state": create_residentstate().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_residentactiontypes(self):
        residentactiontypes = create_residentactiontypes()
        url = reverse('home_residentactiontypes_detail', args=[residentactiontypes.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_residentactiontypes(self):
        residentactiontypes = create_residentactiontypes()
        data = {
            "value": "value",
            "result_state": create_residentstate().pk,
        }
        url = reverse('home_residentactiontypes_update', args=[residentactiontypes.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ResidentResponseViewTest(unittest.TestCase):
    '''
    Tests for ResidentResponse
    '''
    def setUp(self):
        self.client = Client()

    def test_list_residentresponse(self):
        url = reverse('home_residentresponse_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_residentresponse(self):
        url = reverse('home_residentresponse_create')
        data = {
            "satisfactory": "satisfactory",
            "resident": create_resident().pk,
            "sensor_value": create_sensorvalue().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_residentresponse(self):
        residentresponse = create_residentresponse()
        url = reverse('home_residentresponse_detail', args=[residentresponse.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_residentresponse(self):
        residentresponse = create_residentresponse()
        data = {
            "satisfactory": "satisfactory",
            "resident": create_resident().pk,
            "sensor_value": create_sensorvalue().pk,
        }
        url = reverse('home_residentresponse_update', args=[residentresponse.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SensorValueViewTest(unittest.TestCase):
    '''
    Tests for SensorValue
    '''
    def setUp(self):
        self.client = Client()

    def test_list_sensorvalue(self):
        url = reverse('home_sensorvalue_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sensorvalue(self):
        url = reverse('home_sensorvalue_create')
        data = {
            "time": "time",
            "value": "value",
            "sensor": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sensorvalue(self):
        sensorvalue = create_sensorvalue()
        url = reverse('home_sensorvalue_detail', args=[sensorvalue.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sensorvalue(self):
        sensorvalue = create_sensorvalue()
        data = {
            "time": "time",
            "value": "value",
            "sensor": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('home_sensorvalue_update', args=[sensorvalue.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SensorTypeViewTest(unittest.TestCase):
    '''
    Tests for SensorType
    '''
    def setUp(self):
        self.client = Client()

    def test_list_sensortype(self):
        url = reverse('home_sensortype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sensortype(self):
        url = reverse('home_sensortype_create')
        data = {
            "value": "value",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sensortype(self):
        sensortype = create_sensortype()
        url = reverse('home_sensortype_detail', args=[sensortype.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sensortype(self):
        sensortype = create_sensortype()
        data = {
            "value": "value",
        }
        url = reverse('home_sensortype_update', args=[sensortype.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DeviceTimeViewTest(unittest.TestCase):
    '''
    Tests for DeviceTime
    '''
    def setUp(self):
        self.client = Client()

    def test_list_devicetime(self):
        url = reverse('home_devicetime_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_devicetime(self):
        url = reverse('home_devicetime_create')
        data = {
            "start_time": "start_time",
            "finish_time": "finish_time",
            "device": create_device().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_devicetime(self):
        devicetime = create_devicetime()
        url = reverse('home_devicetime_detail', args=[devicetime.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_devicetime(self):
        devicetime = create_devicetime()
        data = {
            "start_time": "start_time",
            "finish_time": "finish_time",
            "device": create_device().pk,
        }
        url = reverse('home_devicetime_update', args=[devicetime.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


