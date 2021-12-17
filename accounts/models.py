from django.core.validators import RegexValidator
from django.db import models

class Bank(models.Model):
    code = models.CharField('Code', max_length=3, validators=[RegexValidator(r'^\d{3}$', message='Enter only 3 numbers')], unique=True)
    name = models.CharField('Name', max_length=255)

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'

    def __str__(self):
        return self.name

# Create your models here.
class Account(models.Model):
    bank = models.ForeignKey(Bank, related_name='bank', on_delete=models.CASCADE)
    number = models.CharField('Number', max_length=16, validators=[RegexValidator(r'^\d{16}$', message='Enter only 16 numbers')], unique=True)
    name = models.CharField('Name', max_length=255)
    validity = models.DateField('Validity', auto_now=True)
    balance = models.DecimalField('Balance', default=0, max_digits=19, decimal_places=2)
    limit = models.DecimalField('Limite', default=100, max_digits=19, decimal_places=2)
    cvv = models.CharField('Card Verification Value', max_length=4, validators=[RegexValidator(r'^\d{4}$', message='Enter only 4 numbers')], unique=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return f'{self.number} - {self.bank} - {self.name}'