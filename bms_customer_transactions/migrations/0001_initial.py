# Generated by Django 3.2.7 on 2021-10-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bms_cu_booking_history',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('pl_id', models.IntegerField()),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('total_price_paid', models.IntegerField()),
                ('mode_of_payment', models.CharField(default='Offline', max_length=20)),
                ('feedback', models.CharField(max_length=2000, null=True)),
            ],
        ),
    ]
