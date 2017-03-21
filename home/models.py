# coding=utf-8
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
    name = models.CharField(max_length=255, verbose_name=u'Название')

    # Relationship Fields
    room = models.ForeignKey('home.room', verbose_name=u'Комната')
    type = models.OneToOneField('home.DeviceType', verbose_name=u'Тип')

    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Устройство"
        verbose_name_plural = u"Устройства"

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('home_device_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_device_update', args=(self.pk,))


class Room(models.Model):

    # Fields
    name = models.CharField(max_length=255, verbose_name=u'Название')
    area = models.FloatField(verbose_name=u'Площадь пола')
    height = models.FloatField(verbose_name=u'Высота стен')


    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Комната"
        verbose_name_plural = u"Комнаты"


    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('home_room_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_room_update', args=(self.pk,))


class Sensor(models.Model):

    # Fields
    name = models.CharField(max_length=255, verbose_name=u'Название')
    min_value = models.IntegerField(verbose_name=u'Минимальное значение')
    max_value = models.IntegerField(verbose_name=u'Максимальное значение')

    # Relationship Fields
    room = models.ForeignKey('home.room', verbose_name=u'Комната')
    type = models.ForeignKey('home.SensorType', verbose_name=u'Тип')

    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Датчик"
        verbose_name_plural = u"Датчики"

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('home_sensor_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('home_sensor_update', args=(self.pk,))


class DeviceType(models.Model):

    # Fields
    value = models.CharField(max_length=255, verbose_name=u'Название')

    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Тип устройства"
        verbose_name_plural = u"Типы устройства"

    def __unicode__(self):
        return u'%s' % self.value

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
    first_name = models.CharField(max_length=30, blank=False, verbose_name=u'Имя')
    last_name = models.CharField(max_length=50, blank=True, verbose_name=u'Фамилия')
    sex = models.CharField(max_length=1, choices=genders, default='M', verbose_name=u'Пол')
    age = models.FloatField(blank=True, verbose_name=u'Возраст')

    # Relationship Fields
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    state = models.ForeignKey('home.ResidentState', verbose_name=u'Состояние')

    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Житель"
        verbose_name_plural = u"Жители"

    def __unicode__(self):
        return u'%s' % self.first_name

    def get_absolute_url(self):
        return reverse('home_resident_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('home_resident_update', args=(self.pk,))


class ResidentState(models.Model):

    # Fields
    value = models.CharField(max_length=255, verbose_name=u'Значение')


    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Состояние жителя"
        verbose_name_plural = u"Состояния жителя"

    def __unicode__(self):
        return u'%s' % self.value

    def get_absolute_url(self):
        return reverse('home_residentstate_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('home_residentstate_update', args=(self.pk,))


class ResidentActions(models.Model):

    # Fields
    time = models.DateTimeField(verbose_name=u'Время')

    # Relationship Fields
    type = models.ForeignKey('home.ResidentActionTypes', verbose_name=u'Тип')
    resident = models.ForeignKey('home.Resident', verbose_name=u'Житель')

    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Действие пользователя"
        verbose_name_plural = u"Действия пользователя"

    def __unicode__(self):
        return u'%s %s action' % (self.resident, self.type)

    def get_absolute_url(self):
        return reverse('home_residentactions_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_residentactions_update', args=(self.pk,))


class ResidentActionTypes(models.Model):

    # Fields
    value = models.CharField(max_length=255, verbose_name=u'Название')

    # Relationship Fields
    result_state = models.ForeignKey('home.ResidentState', verbose_name=u'Состояние жителя')

    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Тип действия пользователя"
        verbose_name_plural = u"Типы действия пользователя"

    def __unicode__(self):
        return u'%s' % self.value

    def get_absolute_url(self):
        return reverse('home_residentactiontypes_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_residentactiontypes_update', args=(self.pk,))


class ResidentResponse(models.Model):

    # Fields
    satisfactory = models.BooleanField(verbose_name=u'Удовлетворен ли')

    # Relationship Fields
    resident = models.ForeignKey('home.Resident', verbose_name=u'Житель')
    sensor_value = models.ForeignKey('home.SensorValue', verbose_name=u'Значения датчиков')

    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Отзыв пользователя"
        verbose_name_plural = u"Отзывы пользователя"

    def __unicode__(self):
        return u"%s  's response" % self.resident

    def get_absolute_url(self):
        return reverse('home_residentresponse_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('home_residentresponse_update', args=(self.pk,))


class SensorValue(models.Model):

    # Fields
    time = models.DateTimeField(verbose_name=u'Время')
    value = models.FloatField(verbose_name=u'Значение')

    # Relationship Fields
    sensor = models.ForeignKey(Sensor, verbose_name=u'Датчик')

    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Значение датчика"
        verbose_name_plural = u"Значения датчика"

    def __unicode__(self):
        return u'%s value' % self.sensor

    def get_absolute_url(self):
        return reverse('home_sensorvalue_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('home_sensorvalue_update', args=(self.pk,))


class SensorType(models.Model):

    # Fields
    value = models.CharField(max_length=30, verbose_name=u'Название')

    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Тип датчика"
        verbose_name_plural = u"Типы дачтика"

    def __unicode__(self):
        return u'%s' % self.value

    def get_absolute_url(self):
        return reverse('home_sensortype_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_sensortype_update', args=(self.pk,))


class DeviceTime(models.Model):

    # Fields
    start_time = models.DateTimeField(verbose_name=u'Время начала работы')
    finish_time = models.DateTimeField(verbose_name=u'Время окончания работы')

    # Relationship Fields
    device = models.ForeignKey('home.Device', verbose_name=u'Устройство')

    class Meta:
        ordering = ('-pk',)
        verbose_name = u"Время работы устройства"
        verbose_name_plural = u"Время работы устройств"

    def __unicode__(self):
        return u'Время %s' % self.device

    def get_absolute_url(self):
        return reverse('home_devicetime_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('home_devicetime_update', args=(self.pk,))


