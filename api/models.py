from django.db import models
from accounts.models import Account

# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(Account, related_name='account', on_delete=models.CASCADE)
    description = models.CharField('Description', max_length=255)
    date = models.DateTimeField('Date', auto_now=True)
    value = models.DecimalField('Value', default=0, max_digits=19, decimal_places=2)
    function = models.CharField('Function', max_length=1, default='D', choices=[('D', 'Debit'), ('C', 'Credit')])

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'