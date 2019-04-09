# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accelerometer(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    double_values_0 = models.CharField(max_length=255, blank=True, null=True)
    double_values_1 = models.CharField(max_length=255, blank=True, null=True)
    double_values_2 = models.CharField(max_length=255, blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accelerometer'


class ApplicationsCrashes(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    package_name = models.TextField(blank=True, null=True)
    application_name = models.TextField(blank=True, null=True)
    application_version = models.FloatField(blank=True, null=True)
    error_short = models.TextField(blank=True, null=True)
    error_long = models.TextField(blank=True, null=True)
    error_condition = models.IntegerField(blank=True, null=True)
    is_system_app = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applications_crashes'


class ApplicationsForeground(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    package_name = models.TextField(blank=True, null=True)
    application_name = models.TextField(blank=True, null=True)
    is_system_app = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applications_foreground'


class ApplicationsHistory(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    package_name = models.TextField(blank=True, null=True)
    application_name = models.TextField(blank=True, null=True)
    process_importance = models.IntegerField(blank=True, null=True)
    process_id = models.IntegerField(blank=True, null=True)
    double_end_timestamp = models.FloatField(blank=True, null=True)
    is_system_app = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applications_history'


class ApplicationsNotifications(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    package_name = models.TextField(blank=True, null=True)
    application_name = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    sound = models.TextField(blank=True, null=True)
    vibrate = models.TextField(blank=True, null=True)
    defaults = models.IntegerField(blank=True, null=True)
    flags = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applications_notifications'


class AwareDevice(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(unique=True, max_length=150, blank=True, null=True)
    board = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    device = models.TextField(blank=True, null=True)
    build_id = models.TextField(blank=True, null=True)
    hardware = models.TextField(blank=True, null=True)
    manufacturer = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    product = models.TextField(blank=True, null=True)
    serial = models.TextField(blank=True, null=True)
    release = models.TextField(blank=True, null=True)
    release_type = models.TextField(blank=True, null=True)
    sdk = models.TextField(blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aware_device'


class AwareLog(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    log_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aware_log'


class AwareStudies(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    study_url = models.TextField(blank=True, null=True)
    study_key = models.IntegerField(blank=True, null=True)
    study_api = models.TextField(blank=True, null=True)
    study_pi = models.TextField(blank=True, null=True)
    study_config = models.TextField(blank=True, null=True)
    study_title = models.TextField(blank=True, null=True)
    study_description = models.TextField(blank=True, null=True)
    double_join = models.FloatField(blank=True, null=True)
    double_exit = models.FloatField(blank=True, null=True)
    study_compliance = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aware_studies'


class Barometer(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    double_values_0 = models.CharField(max_length=255, blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barometer'


class Battery(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    battery_status = models.IntegerField(blank=True, null=True)
    battery_level = models.IntegerField(blank=True, null=True)
    battery_scale = models.IntegerField(blank=True, null=True)
    battery_voltage = models.IntegerField(blank=True, null=True)
    battery_temperature = models.IntegerField(blank=True, null=True)
    battery_adaptor = models.IntegerField(blank=True, null=True)
    battery_health = models.IntegerField(blank=True, null=True)
    battery_technology = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'battery'


class BatteryCharges(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    battery_start = models.IntegerField(blank=True, null=True)
    battery_end = models.IntegerField(blank=True, null=True)
    double_end_timestamp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'battery_charges'


class BatteryDischarges(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    battery_start = models.IntegerField(blank=True, null=True)
    battery_end = models.IntegerField(blank=True, null=True)
    double_end_timestamp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'battery_discharges'


class Bluetooth(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    bt_address = models.CharField(max_length=150, blank=True, null=True)
    bt_name = models.TextField(blank=True, null=True)
    bt_rssi = models.IntegerField(blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bluetooth'


class Calls(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    call_type = models.IntegerField(blank=True, null=True)
    call_duration = models.IntegerField(blank=True, null=True)
    trace = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calls'


class Keyboard(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    package_name = models.CharField(max_length=255, blank=True, null=True)
    before_text = models.CharField(max_length=255, blank=True, null=True)
    current_text = models.CharField(max_length=255, blank=True, null=True)
    is_password = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyboard'


class Light(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    double_light_lux = models.CharField(max_length=255, blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'light'


class Locations(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    device_id = models.CharField(max_length=255, blank=True, null=True)
    double_latitude = models.CharField(max_length=255, blank=True, null=True)
    double_longitude = models.CharField(max_length=255, blank=True, null=True)
    double_bearing = models.CharField(max_length=255, blank=True, null=True)
    double_speed = models.CharField(max_length=255, blank=True, null=True)
    double_altitude = models.CharField(max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    accuracy = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Messages(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    message_type = models.IntegerField(blank=True, null=True)
    trace = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class MqttHistory(models.Model):
    timestamp = models.FloatField()
    topic = models.TextField()
    message = models.TextField()
    receivers = models.TextField()

    class Meta:
        managed = False
        db_table = 'mqtt_history'


class MqttMessages(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mqtt_messages'


class MqttSubscriptions(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    topic = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mqtt_subscriptions'


class Network(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    network_type = models.IntegerField(blank=True, null=True)
    network_subtype = models.TextField(blank=True, null=True)
    network_state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'network'


class NetworkTraffic(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    network_type = models.IntegerField(blank=True, null=True)
    double_received_bytes = models.FloatField(blank=True, null=True)
    double_sent_bytes = models.FloatField(blank=True, null=True)
    double_received_packets = models.FloatField(blank=True, null=True)
    double_sent_packets = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'network_traffic'


class Screen(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    screen_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'screen'


class SensorBluetooth(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    bt_address = models.CharField(max_length=150, blank=True, null=True)
    bt_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_bluetooth'


class Wifi(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    timestamp = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    bssid = models.CharField(max_length=255, blank=True, null=True)
    ssid = models.CharField(max_length=255, blank=True, null=True)
    security = models.CharField(max_length=255, blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    rssi = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wifi'
