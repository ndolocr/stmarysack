from django.db import models
from django.utils.translation import ugettext_lazy as _

'''
	This app creates church events.
	Events are all occurences that are 
	expected to occur in church together
	with their respective dates. This app
	the church advertise and let its member
	know the events that will occur in the church.
'''

class Event(models.Model):
	date_to = models.DateField(_('To'))
	date_from = models.DateField(_('From'))
	event_description = models.TextField(_('Event Description'))
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	event_name = models.CharField(_('Event Name'), max_length=255, blank=False, null=False)

	class Meta:
		verbose_name = "Event"
		verbose_name_plural = "Events"

	def __str__(self):
		return self.event_name