from django.db import models
from django.conf import settings
from accounts.models import Member
from contributionType.models import ContributionType
from django.utils.translation import gettext_lazy as _

'''
	This is the contribution Application.
	Members of the church contribute cash 
	adn other materials to the church. The 
	members contributions are recorded here for future reference.
'''

class Contribution(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE, default=1)
	contribution_type = models.ManyToManyField(ContributionType)
	amount = models.PositiveIntegerField(_('Amount in Ksh.'))
	date_of_contribution = models.DateField(_('Date'), blank=False, null=False)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)

	class Meta:
		verbose_name = 'Contribution'
		verbose_name_plural = 'Contributions'

	def __str__(self):
		contributor = "{} - {} - {}".format(self.member, self.amount, self.date_of_contribution)
		return contributor
