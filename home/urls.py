from django.conf.urls import url, include
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'device', api.DeviceViewSet)
router.register(r'room', api.RoomViewSet)
router.register(r'sensor', api.SensorViewSet)
router.register(r'devicetype', api.DeviceTypeViewSet)
router.register(r'resident', api.ResidentViewSet)
router.register(r'residentstate', api.ResidentStateViewSet)
router.register(r'residentactions', api.ResidentActionsViewSet)
router.register(r'residentactiontypes', api.ResidentActionTypesViewSet)
router.register(r'residentresponse', api.ResidentResponseViewSet)
router.register(r'sensorvalue', api.SensorValueViewSet)
router.register(r'sensortype', api.SensorTypeViewSet)
router.register(r'devicetime', api.DeviceTimeViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Device
    url(r'^home/device/$', views.DeviceListView.as_view(), name='home_device_list'),
    url(r'^home/device/create/$', views.DeviceCreateView.as_view(), name='home_device_create'),
    url(r'^home/device/detail/(?P<pk>\S+)/$', views.DeviceDetailView.as_view(), name='home_device_detail'),
    url(r'^home/device/update/(?P<pk>\S+)/$', views.DeviceUpdateView.as_view(), name='home_device_update'),
)

urlpatterns += (
    # urls for Room
    url(r'^home/room/$', views.RoomListView.as_view(), name='home_room_list'),
    url(r'^home/room/create/$', views.RoomCreateView.as_view(), name='home_room_create'),
    url(r'^home/room/detail/(?P<pk>\S+)/$', views.RoomDetailView.as_view(), name='home_room_detail'),
    url(r'^home/room/update/(?P<pk>\S+)/$', views.RoomUpdateView.as_view(), name='home_room_update'),
)

urlpatterns += (
    # urls for Sensor
    url(r'^home/sensor/$', views.SensorListView.as_view(), name='home_sensor_list'),
    url(r'^home/sensor/create/$', views.SensorCreateView.as_view(), name='home_sensor_create'),
    url(r'^home/sensor/detail/(?P<pk>\S+)/$', views.SensorDetailView.as_view(), name='home_sensor_detail'),
    url(r'^home/sensor/update/(?P<pk>\S+)/$', views.SensorUpdateView.as_view(), name='home_sensor_update'),
)

urlpatterns += (
    # urls for DeviceType
    url(r'^home/devicetype/$', views.DeviceTypeListView.as_view(), name='home_devicetype_list'),
    url(r'^home/devicetype/create/$', views.DeviceTypeCreateView.as_view(), name='home_devicetype_create'),
    url(r'^home/devicetype/detail/(?P<pk>\S+)/$', views.DeviceTypeDetailView.as_view(), name='home_devicetype_detail'),
    url(r'^home/devicetype/update/(?P<pk>\S+)/$', views.DeviceTypeUpdateView.as_view(), name='home_devicetype_update'),
)

urlpatterns += (
    # urls for Resident
    url(r'^home/resident/$', views.ResidentListView.as_view(), name='home_resident_list'),
    url(r'^home/resident/create/$', views.ResidentCreateView.as_view(), name='home_resident_create'),
    url(r'^home/resident/detail/(?P<pk>\S+)/$', views.ResidentDetailView.as_view(), name='home_resident_detail'),
    url(r'^home/resident/update/(?P<pk>\S+)/$', views.ResidentUpdateView.as_view(), name='home_resident_update'),
)

urlpatterns += (
    # urls for ResidentState
    url(r'^home/residentstate/$', views.ResidentStateListView.as_view(), name='home_residentstate_list'),
    url(r'^home/residentstate/create/$', views.ResidentStateCreateView.as_view(), name='home_residentstate_create'),
    url(r'^home/residentstate/detail/(?P<pk>\S+)/$', views.ResidentStateDetailView.as_view(), name='home_residentstate_detail'),
    url(r'^home/residentstate/update/(?P<pk>\S+)/$', views.ResidentStateUpdateView.as_view(), name='home_residentstate_update'),
)

urlpatterns += (
    # urls for ResidentActions
    url(r'^home/residentactions/$', views.ResidentActionsListView.as_view(), name='home_residentactions_list'),
    url(r'^home/residentactions/create/$', views.ResidentActionsCreateView.as_view(), name='home_residentactions_create'),
    url(r'^home/residentactions/detail/(?P<pk>\S+)/$', views.ResidentActionsDetailView.as_view(), name='home_residentactions_detail'),
    url(r'^home/residentactions/update/(?P<pk>\S+)/$', views.ResidentActionsUpdateView.as_view(), name='home_residentactions_update'),
)

urlpatterns += (
    # urls for ResidentActionTypes
    url(r'^home/residentactiontypes/$', views.ResidentActionTypesListView.as_view(), name='home_residentactiontypes_list'),
    url(r'^home/residentactiontypes/create/$', views.ResidentActionTypesCreateView.as_view(), name='home_residentactiontypes_create'),
    url(r'^home/residentactiontypes/detail/(?P<pk>\S+)/$', views.ResidentActionTypesDetailView.as_view(), name='home_residentactiontypes_detail'),
    url(r'^home/residentactiontypes/update/(?P<pk>\S+)/$', views.ResidentActionTypesUpdateView.as_view(), name='home_residentactiontypes_update'),
)

urlpatterns += (
    # urls for ResidentResponse
    url(r'^home/residentresponse/$', views.ResidentResponseListView.as_view(), name='home_residentresponse_list'),
    url(r'^home/residentresponse/create/$', views.ResidentResponseCreateView.as_view(), name='home_residentresponse_create'),
    url(r'^home/residentresponse/detail/(?P<pk>\S+)/$', views.ResidentResponseDetailView.as_view(), name='home_residentresponse_detail'),
    url(r'^home/residentresponse/update/(?P<pk>\S+)/$', views.ResidentResponseUpdateView.as_view(), name='home_residentresponse_update'),
)

urlpatterns += (
    # urls for SensorValue
    url(r'^home/sensorvalue/$', views.SensorValueListView.as_view(), name='home_sensorvalue_list'),
    url(r'^home/sensorvalue/create/$', views.SensorValueCreateView.as_view(), name='home_sensorvalue_create'),
    url(r'^home/sensorvalue/detail/(?P<pk>\S+)/$', views.SensorValueDetailView.as_view(), name='home_sensorvalue_detail'),
    url(r'^home/sensorvalue/update/(?P<pk>\S+)/$', views.SensorValueUpdateView.as_view(), name='home_sensorvalue_update'),
)

urlpatterns += (
    # urls for SensorType
    url(r'^home/sensortype/$', views.SensorTypeListView.as_view(), name='home_sensortype_list'),
    url(r'^home/sensortype/create/$', views.SensorTypeCreateView.as_view(), name='home_sensortype_create'),
    url(r'^home/sensortype/detail/(?P<pk>\S+)/$', views.SensorTypeDetailView.as_view(), name='home_sensortype_detail'),
    url(r'^home/sensortype/update/(?P<pk>\S+)/$', views.SensorTypeUpdateView.as_view(), name='home_sensortype_update'),
)

urlpatterns += (
    # urls for DeviceTime
    url(r'^home/devicetime/$', views.DeviceTimeListView.as_view(), name='home_devicetime_list'),
    url(r'^home/devicetime/create/$', views.DeviceTimeCreateView.as_view(), name='home_devicetime_create'),
    url(r'^home/devicetime/detail/(?P<pk>\S+)/$', views.DeviceTimeDetailView.as_view(), name='home_devicetime_detail'),
    url(r'^home/devicetime/update/(?P<pk>\S+)/$', views.DeviceTimeUpdateView.as_view(), name='home_devicetime_update'),
)

