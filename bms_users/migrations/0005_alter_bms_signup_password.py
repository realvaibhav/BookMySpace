# Generated by Django 3.2.7 on 2021-11-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms_users', '0004_auto_20211015_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bms_signup',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]