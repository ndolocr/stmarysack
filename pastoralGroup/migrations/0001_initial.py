# Generated by Django 2.1.2 on 2018-10-24 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PastoralGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pastoral_group', models.CharField(max_length=255, verbose_name='Pastoral Group')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated On')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
            ],
            options={
                'verbose_name': 'Pastoral Group',
                'verbose_name_plural': 'Pastoral Groups',
            },
        ),
    ]
