# Generated by Django 2.1.2 on 2018-10-26 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20181026_1230'),
        ('contributionType', '0003_auto_20181025_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Amount in Ksh.')),
                ('date_of_contribution', models.DateField(verbose_name='Date')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated On')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('contribution_type', models.ManyToManyField(to='contributionType.ContributionType')),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('member', models.ManyToManyField(to='accounts.Member')),
            ],
            options={
                'verbose_name': 'Contribution',
                'verbose_name_plural': 'Contributions',
            },
        ),
    ]
