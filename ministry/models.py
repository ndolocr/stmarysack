from django.db import models
from django.utils.translation import ugettext_lazy as _

'''
	This Model creates the Ministry app.
	Ministries are used to group christians 
	in groups accoring to one's preference in
	the church activities. Groups include the choir,
	Youth groups, Men Groups, Women groups among other groups.
'''

class Ministry(models.Model):		
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	ministry = models.CharField(_('Ministry'), max_length=255, blank=False,null=False)

	class Meta:
		verbose_name = "Ministry"
		verbose_name_plural = "Ministries"

	def __str__(self):
		return self.ministry