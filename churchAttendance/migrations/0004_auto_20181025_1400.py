# Generated by Django 2.1.2 on 2018-10-25 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('churchAttendance', '0003_auto_20181025_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='churchattendance',
            name='user',
        ),
        migrations.AddField(
            model_name='churchattendance',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
