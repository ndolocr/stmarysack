from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

'''
	This creates the services app.
	This app creates the different
	services that occur in the church.
	Records on the service name and time are recorded.
'''

class Service(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	service_name = models.CharField(_('Service Name'), max_length=255, blank=False, null=False)
	service_time = models.TimeField(_('Service Time'), blank=False, null=False)

	class Meta:
		verbose_name = "Service"
		verbose_name_plural = "Services"

	def __str__(self):
		return self.service_name