# Generated by Django 5.1.6 on 2025-03-07 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airplane', '0001_initial'),
        ('bus', '0001_initial'),
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('national_id', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airplane.airplane')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.bus')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.train')),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserve_passenger', to='detail.passenger')),
                ('ticket_airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserve_passenger', to='detail.ticket_airplane')),
                ('ticket_bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserve_passenger', to='detail.ticket_bus')),
                ('ticket_train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserve_passenger', to='detail.ticket_train')),
            ],
        ),
    ]
