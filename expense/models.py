from django.db import models
from django.utils.translation import ugettext_lazy as _

'''
	This is the expenses App.
	This application records all 
	the expenses incured by the church.
'''

class Expense(models.Model):
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	voucher_no = models.CharField(_('Voucher Number'), max_length=255, blank=True, null=True)
	expense_date = models.DateField(_('Date'), blank=False, null=False)
	expense_amount = models.IntegerField(_('Amount in Ksh.'), blank=False, null=False)
	expense_description = models.TextField(_('Expense Description'), blank=False, null=False)

	class Meta:
		verbose_name = "Expense"
		verbose_name_plural = "Expenses"

	def __str__(self):
		return self.voucher_no