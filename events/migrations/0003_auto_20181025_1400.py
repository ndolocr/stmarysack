# Generated by Django 2.1.2 on 2018-10-25 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='user',
            new_name='created_by',
        ),
    ]
