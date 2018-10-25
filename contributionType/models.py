from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

'''
	This app creates the Contribution Types.
	There are many different contributions in 
	church and this app is used to classify the 
	types of contributions available. They include:
	Tithe, sunday offering during the service, Thanks Giving, Develpoment among others.
'''

class ContributionType(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	contribution_type = models.CharField(_('Contribution Type'), max_length=255, blank=False, null=False)

	class Meta:
		verbose_name = "Contribution Type"
		verbose_name_plural = "Contribution Types"

	def __str__(self):
		return self.contribution_type
