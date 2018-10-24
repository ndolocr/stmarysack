from django.db import models
from django.utils.translation import ugettext_lazy as _

	'''
		This Model is used to create and save ministry information where members
		belong to!
	'''

	class Ministry(models.Model):		
		updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
		created_on = models.DateTimeField(_('Created On'), auto_add_now=True)
		ministry = models.CharField(_('Ministry'), max_length=255, blank=False,null=False)