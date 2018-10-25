from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

'''
	This app creates the Pastoral Group.
	Pastoral Groups are used to group christian
	communities according to the places they live in.
	They help neighbours who worship in the same church 
	know each other, interact and they act as the first set 
	of friends christians can go to for help when a need arises.
'''

class PastoralGroup(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	pastoral_group = models.CharField(_('Pastoral Group'), max_length=255, blank=False, null=False)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)

	class Meta:
		verbose_name = "Pastoral Group"
		verbose_name_plural = "Pastoral Groups"

	def __str__(self):
		return self.pastoral_group
