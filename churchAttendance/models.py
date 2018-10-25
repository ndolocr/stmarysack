from django.db import models
from django.conf import settings
from service.models import Service
from django.utils.translation import ugettext_lazy as _

'''
	This is the church attendance app.
	I this App, records about the number 
	of people attending a service is recorded.	
'''

class ChurchAttendance(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	attendance = models.PositiveIntegerField(_('Attendance'), blank=False, null=False)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	attendance_date = models.DateField(_('Date'), blank=False, null=False)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)

	class Meta:
		verbose_name = "Church Attendance"
		verbose_name_plural = "Church Attendances"

	def __str__(self):
		attendance_name = "{} - {}".format(self.service, self.attendance_date)
		return attendance_name