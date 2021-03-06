# Generated by Django 2.1.2 on 2018-10-24 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.PositiveIntegerField(verbose_name='Attendance')),
                ('attendance_date', models.DateField(verbose_name='Date')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated On')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service')),
            ],
            options={
                'verbose_name': 'Church Attendance',
                'verbose_name_plural': 'Church Attendances',
            },
        ),
    ]
