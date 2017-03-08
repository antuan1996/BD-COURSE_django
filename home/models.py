from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Device(models.Model):

    # Fields
    name = models.CharField(max_length=255)

    # Relationship Fields
    room = models.ForeignKey('home.room', )
    type = models.OneToOneField('home.DeviceType', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_device_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_device_update', args=(self.pk,))


class Room(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    area = models.FloatField()
    height = models.FloatField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_room_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_room_update', args=(self.pk,))


class Sensor(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    min_value = models.IntegerField()
    max_value = models.IntegerField()

    # Relationship Fields
    room = models.ForeignKey('home.room', )
    type = models.ForeignKey('home.SensorType', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_sensor_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_sensor_update', args=(self.pk,))


class DeviceType(models.Model):

    # Fields
    value = models.CharField(max_length=255)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_devicetype_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_devicetype_update', args=(self.pk,))


class Resident(models.Model):
    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Other')
    )

    # Fields
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=50, blank=True)
    sex = models.CharField(max_length=1, choices=genders, default='M')
    age = models.FloatField(blank=True)

    # Relationship Fields
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    state = models.ForeignKey('home.ResidentState', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_resident_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_resident_update', args=(self.pk,))


class ResidentState(models.Model):

    # Fields
    value = models.CharField(max_length=255)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_residentstate_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_residentstate_update', args=(self.pk,))


class ResidentActions(models.Model):

    # Fields
    time = models.DateTimeField()

    # Relationship Fields
    type = models.ForeignKey('home.ResidentActionTypes', )
    resident = models.ForeignKey('home.Resident', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_residentactions_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_residentactions_update', args=(self.pk,))


class ResidentActionTypes(models.Model):

    # Fields
    value = models.CharField(max_length=255)

    # Relationship Fields
    result_state = models.ForeignKey('home.ResidentState', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_residentactiontypes_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_residentactiontypes_update', args=(self.pk,))


class ResidentResponse(models.Model):

    # Fields
    satisfactory = models.BooleanField()

    # Relationship Fields
    resident = models.ForeignKey('home.Resident', )
    sensor_value = models.ForeignKey('home.SensorValue', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_residentresponse_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_residentresponse_update', args=(self.pk,))


class SensorValue(models.Model):

    # Fields
    time = models.DateTimeField()
    value = models.FloatField()

    # Relationship Fields
    sensor = models.ForeignKey(Sensor, )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_sensorvalue_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_sensorvalue_update', args=(self.pk,))


class SensorType(models.Model):

    # Fields
    value = models.CharField(max_length=30)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_sensortype_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_sensortype_update', args=(self.pk,))


class DeviceTime(models.Model):

    # Fields
    start_time = models.DateTimeField()
    finish_time = models.TextField(max_length=100)

    # Relationship Fields
    device = models.ForeignKey('home.Device', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_devicetime_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_devicetime_update', args=(self.pk,))


