# Generated by Django 2.1.7 on 2019-04-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accelerometer',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.CharField(blank=True, max_length=255, null=True)),
                ('device_id', models.CharField(blank=True, max_length=255, null=True)),
                ('double_values_0', models.CharField(blank=True, max_length=255, null=True)),
                ('double_values_1', models.CharField(blank=True, max_length=255, null=True)),
                ('double_values_2', models.CharField(blank=True, max_length=255, null=True)),
                ('accuracy', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'accelerometer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationsCrashes',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('package_name', models.TextField(blank=True, null=True)),
                ('application_name', models.TextField(blank=True, null=True)),
                ('application_version', models.FloatField(blank=True, null=True)),
                ('error_short', models.TextField(blank=True, null=True)),
                ('error_long', models.TextField(blank=True, null=True)),
                ('error_condition', models.IntegerField(blank=True, null=True)),
                ('is_system_app', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'applications_crashes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationsForeground',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('package_name', models.TextField(blank=True, null=True)),
                ('application_name', models.TextField(blank=True, null=True)),
                ('is_system_app', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'applications_foreground',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationsHistory',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('package_name', models.TextField(blank=True, null=True)),
                ('application_name', models.TextField(blank=True, null=True)),
                ('process_importance', models.IntegerField(blank=True, null=True)),
                ('process_id', models.IntegerField(blank=True, null=True)),
                ('double_end_timestamp', models.FloatField(blank=True, null=True)),
                ('is_system_app', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'applications_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationsNotifications',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('package_name', models.TextField(blank=True, null=True)),
                ('application_name', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('sound', models.TextField(blank=True, null=True)),
                ('vibrate', models.TextField(blank=True, null=True)),
                ('defaults', models.IntegerField(blank=True, null=True)),
                ('flags', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'applications_notifications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AwareDevice',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('board', models.TextField(blank=True, null=True)),
                ('brand', models.TextField(blank=True, null=True)),
                ('device', models.TextField(blank=True, null=True)),
                ('build_id', models.TextField(blank=True, null=True)),
                ('hardware', models.TextField(blank=True, null=True)),
                ('manufacturer', models.TextField(blank=True, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('product', models.TextField(blank=True, null=True)),
                ('serial', models.TextField(blank=True, null=True)),
                ('release', models.TextField(blank=True, null=True)),
                ('release_type', models.TextField(blank=True, null=True)),
                ('sdk', models.TextField(blank=True, null=True)),
                ('label', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aware_device',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AwareLog',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('log_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aware_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AwareStudies',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('study_url', models.TextField(blank=True, null=True)),
                ('study_key', models.IntegerField(blank=True, null=True)),
                ('study_api', models.TextField(blank=True, null=True)),
                ('study_pi', models.TextField(blank=True, null=True)),
                ('study_config', models.TextField(blank=True, null=True)),
                ('study_title', models.TextField(blank=True, null=True)),
                ('study_description', models.TextField(blank=True, null=True)),
                ('double_join', models.FloatField(blank=True, null=True)),
                ('double_exit', models.FloatField(blank=True, null=True)),
                ('study_compliance', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aware_studies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Barometer',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.CharField(blank=True, max_length=255, null=True)),
                ('device_id', models.CharField(blank=True, max_length=255, null=True)),
                ('double_values_0', models.CharField(blank=True, max_length=255, null=True)),
                ('accuracy', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'barometer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('battery_status', models.IntegerField(blank=True, null=True)),
                ('battery_level', models.IntegerField(blank=True, null=True)),
                ('battery_scale', models.IntegerField(blank=True, null=True)),
                ('battery_voltage', models.IntegerField(blank=True, null=True)),
                ('battery_temperature', models.IntegerField(blank=True, null=True)),
                ('battery_adaptor', models.IntegerField(blank=True, null=True)),
                ('battery_health', models.IntegerField(blank=True, null=True)),
                ('battery_technology', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'battery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BatteryCharges',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('battery_start', models.IntegerField(blank=True, null=True)),
                ('battery_end', models.IntegerField(blank=True, null=True)),
                ('double_end_timestamp', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'battery_charges',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BatteryDischarges',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('battery_start', models.IntegerField(blank=True, null=True)),
                ('battery_end', models.IntegerField(blank=True, null=True)),
                ('double_end_timestamp', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'battery_discharges',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bluetooth',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('bt_address', models.CharField(blank=True, max_length=150, null=True)),
                ('bt_name', models.TextField(blank=True, null=True)),
                ('bt_rssi', models.IntegerField(blank=True, null=True)),
                ('label', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bluetooth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calls',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('call_type', models.IntegerField(blank=True, null=True)),
                ('call_duration', models.IntegerField(blank=True, null=True)),
                ('trace', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'calls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.CharField(blank=True, max_length=255, null=True)),
                ('device_id', models.CharField(blank=True, max_length=255, null=True)),
                ('package_name', models.CharField(blank=True, max_length=255, null=True)),
                ('before_text', models.CharField(blank=True, max_length=255, null=True)),
                ('current_text', models.CharField(blank=True, max_length=255, null=True)),
                ('is_password', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'keyboard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.CharField(blank=True, max_length=255, null=True)),
                ('device_id', models.CharField(blank=True, max_length=255, null=True)),
                ('double_light_lux', models.CharField(blank=True, max_length=255, null=True)),
                ('accuracy', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'light',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('device_id', models.CharField(blank=True, max_length=255, null=True)),
                ('double_latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('double_longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('double_bearing', models.CharField(blank=True, max_length=255, null=True)),
                ('double_speed', models.CharField(blank=True, max_length=255, null=True)),
                ('double_altitude', models.CharField(blank=True, max_length=255, null=True)),
                ('provider', models.CharField(blank=True, max_length=255, null=True)),
                ('accuracy', models.CharField(blank=True, max_length=255, null=True)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'locations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('message_type', models.IntegerField(blank=True, null=True)),
                ('trace', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'messages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MqttHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.FloatField()),
                ('topic', models.TextField()),
                ('message', models.TextField()),
                ('receivers', models.TextField()),
            ],
            options={
                'db_table': 'mqtt_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MqttMessages',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('topic', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mqtt_messages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MqttSubscriptions',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('topic', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mqtt_subscriptions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('network_type', models.IntegerField(blank=True, null=True)),
                ('network_subtype', models.TextField(blank=True, null=True)),
                ('network_state', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'network',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NetworkTraffic',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('network_type', models.IntegerField(blank=True, null=True)),
                ('double_received_bytes', models.FloatField(blank=True, null=True)),
                ('double_sent_bytes', models.FloatField(blank=True, null=True)),
                ('double_received_packets', models.FloatField(blank=True, null=True)),
                ('double_sent_packets', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'network_traffic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('screen_status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'screen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SensorBluetooth',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('bt_address', models.CharField(blank=True, max_length=150, null=True)),
                ('bt_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sensor_bluetooth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wifi',
            fields=[
                ('field_id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('timestamp', models.CharField(blank=True, max_length=255, null=True)),
                ('device_id', models.CharField(blank=True, max_length=255, null=True)),
                ('bssid', models.CharField(blank=True, max_length=255, null=True)),
                ('ssid', models.CharField(blank=True, max_length=255, null=True)),
                ('security', models.CharField(blank=True, max_length=255, null=True)),
                ('frequency', models.IntegerField(blank=True, null=True)),
                ('rssi', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'wifi',
                'managed': False,
            },
        ),
    ]
