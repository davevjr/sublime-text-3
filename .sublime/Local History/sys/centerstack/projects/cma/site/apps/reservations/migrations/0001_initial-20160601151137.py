# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 15:41
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_xworkflows.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('tours', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bikes', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalReservation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('rental_type', models.CharField(blank=True, choices=[(b'bike', b'Bike'), (b'tour', b'Tour'), (b'tour_bike', b'Tour / Bike'), (b'class', b'Class'), (b'class_bike', b'Class / Bike'), (b'storage', b'Storage')], max_length=20, null=True)),
                ('status', django_xworkflows.models.StateField(max_length=22, workflow=django_xworkflows.models._SerializedWorkflow(initial_state=b'submitted', name=b'Workflow', states=[b'submitted', b'pending_deposit', b'reserved', b'checked_out', b'checked_in', b'damaged', b'pending_damage_payment', b'closed']))),
                ('tour_room_type', models.CharField(blank=True, choices=[(b'Single', b'Single'), (b'Shared', b'Shared')], default=b'Shared', max_length=10, null=True)),
                ('storage_bike', models.CharField(blank=True, max_length=50, null=True)),
                ('checkout_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name=b'Check-Out')),
                ('checkin_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name=b'Check-In')),
                ('start', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('end', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('flexibility', models.CharField(blank=True, choices=[(5, '\xb15 Days'), (4, '\xb14 Days'), (3, '\xb13 Days'), (2, '\xb12 Days'), (1, '\xb11 Day'), (b'Exact', b'Exact')], default=b'Exact', max_length=20, null=True)),
                ('checkout_datetime_actual', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name=b'Check-Out (Actual)')),
                ('checkout_milage', models.IntegerField(blank=True, null=True)),
                ('checkout_img_1', models.TextField(blank=True, max_length=100, null=True)),
                ('checkout_img_2', models.TextField(blank=True, max_length=100, null=True)),
                ('checkout_img_3', models.TextField(blank=True, max_length=100, null=True)),
                ('checkout_img_4', models.TextField(blank=True, max_length=100, null=True)),
                ('checkout_img_5', models.TextField(blank=True, max_length=100, null=True)),
                ('checkout_img_6', models.TextField(blank=True, max_length=100, null=True)),
                ('checkout_notes', models.TextField(blank=True, null=True)),
                ('checkout_file_created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('checkout_file_modified', models.DateTimeField(blank=True, editable=False, null=True)),
                ('checkin_datetime_actual', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name=b'Check-In (Actual)')),
                ('checkin_milage', models.IntegerField(blank=True, null=True)),
                ('is_damaged', models.BooleanField(default=0)),
                ('checkin_img_1', models.TextField(blank=True, max_length=100, null=True)),
                ('checkin_img_2', models.TextField(blank=True, max_length=100, null=True)),
                ('checkin_img_3', models.TextField(blank=True, max_length=100, null=True)),
                ('checkin_img_4', models.TextField(blank=True, max_length=100, null=True)),
                ('checkin_img_5', models.TextField(blank=True, max_length=100, null=True)),
                ('checkin_img_6', models.TextField(blank=True, max_length=100, null=True)),
                ('checkin_notes', models.TextField(blank=True, null=True)),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name=b'Group Discount (%)')),
                ('tax_rate', models.DecimalField(blank=True, decimal_places=2, default=10.0, max_digits=4, null=True, verbose_name=b'Tax Rate (%)')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('modified', models.DateTimeField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('bike', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='bikes.Bike')),
                ('classes', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='classes.Class')),
                ('customer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='customers.Customer')),
                ('group', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='reservations.Group')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tour', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tours.Tour')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical reservation',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_type', models.CharField(blank=True, choices=[(b'bike', b'Bike'), (b'tour', b'Tour'), (b'tour_bike', b'Tour / Bike'), (b'class', b'Class'), (b'class_bike', b'Class / Bike'), (b'storage', b'Storage')], max_length=20, null=True)),
                ('status', django_xworkflows.models.StateField(max_length=22, workflow=django_xworkflows.models._SerializedWorkflow(initial_state=b'submitted', name=b'Workflow', states=[b'submitted', b'pending_deposit', b'reserved', b'checked_out', b'checked_in', b'damaged', b'pending_damage_payment', b'closed']))),
                ('tour_room_type', models.CharField(blank=True, choices=[(b'Single', b'Single'), (b'Shared', b'Shared')], default=b'Shared', max_length=10, null=True)),
                ('storage_bike', models.CharField(blank=True, max_length=50, null=True)),
                ('checkout_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name=b'Check-Out')),
                ('checkin_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name=b'Check-In')),
                ('start', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('end', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('flexibility', models.CharField(blank=True, choices=[(5, '\xb15 Days'), (4, '\xb14 Days'), (3, '\xb13 Days'), (2, '\xb12 Days'), (1, '\xb11 Day'), (b'Exact', b'Exact')], default=b'Exact', max_length=20, null=True)),
                ('checkout_datetime_actual', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name=b'Check-Out (Actual)')),
                ('checkout_milage', models.IntegerField(blank=True, null=True)),
                ('checkout_img_1', models.FileField(blank=True, null=True, upload_to=b'Check-Out/%Y/%m/')),
                ('checkout_img_2', models.FileField(blank=True, null=True, upload_to=b'Check-Out/%Y/%m/')),
                ('checkout_img_3', models.FileField(blank=True, null=True, upload_to=b'Check-Out/%Y/%m/')),
                ('checkout_img_4', models.FileField(blank=True, null=True, upload_to=b'Check-Out/%Y/%m/')),
                ('checkout_img_5', models.FileField(blank=True, null=True, upload_to=b'Check-Out/%Y/%m/')),
                ('checkout_img_6', models.FileField(blank=True, null=True, upload_to=b'Check-Out/%Y/%m/')),
                ('checkout_notes', models.TextField(blank=True, null=True)),
                ('checkout_file_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('checkout_file_modified', models.DateTimeField(auto_now=True, null=True)),
                ('checkin_datetime_actual', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name=b'Check-In (Actual)')),
                ('checkin_milage', models.IntegerField(blank=True, null=True)),
                ('is_damaged', models.BooleanField(default=0)),
                ('checkin_img_1', models.FileField(blank=True, null=True, upload_to=b'Check-In/%Y/%m/')),
                ('checkin_img_2', models.FileField(blank=True, null=True, upload_to=b'Check-In/%Y/%m/')),
                ('checkin_img_3', models.FileField(blank=True, null=True, upload_to=b'Check-In/%Y/%m/')),
                ('checkin_img_4', models.FileField(blank=True, null=True, upload_to=b'Check-In/%Y/%m/')),
                ('checkin_img_5', models.FileField(blank=True, null=True, upload_to=b'Check-In/%Y/%m/')),
                ('checkin_img_6', models.FileField(blank=True, null=True, upload_to=b'Check-In/%Y/%m/')),
                ('checkin_notes', models.TextField(blank=True, null=True)),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name=b'Group Discount (%)')),
                ('tax_rate', models.DecimalField(blank=True, decimal_places=2, default=10.0, max_digits=4, null=True, verbose_name=b'Tax Rate (%)')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('bike', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bikes.Bike')),
                ('bike_accessories', models.ManyToManyField(blank=True, to='bikes.BikeAccessories')),
                ('classes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Class')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.Group')),
            ],
            bases=(django_xworkflows.models.WorkflowEnabled, models.Model),
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('end', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('flexibility', models.CharField(blank=True, choices=[(5, '\xb15 Days'), (4, '\xb14 Days'), (3, '\xb13 Days'), (2, '\xb12 Days'), (1, '\xb11 Day'), (b'Exact', b'Exact')], default=b'Exact', max_length=20, null=True)),
                ('bike', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bikes.Bike')),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.Reservation')),
            ],
        ),
        migrations.CreateModel(
            name='StorageAccessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('price_period', models.CharField(blank=True, choices=[(b'One-Time', b'One-Time'), (b'Daily', b'Daily'), (b'Hourly', b'Hourly'), (b'Monthly', b'Monthly'), (b'Bi-Annual', b'Bi-Annual'), (b'Annual', b'Annual')], default=b'One-Time', max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Storage Accessories',
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='storage_accessories',
            field=models.ManyToManyField(blank=True, to='reservations.StorageAccessories'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.Tour'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='tour_accessories',
            field=models.ManyToManyField(blank=True, to='tours.TourAccessories'),
        ),
    ]
