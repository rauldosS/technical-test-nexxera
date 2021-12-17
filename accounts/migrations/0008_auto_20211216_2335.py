# Generated by Django 3.2.9 on 2021-12-17 02:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20211216_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='cvv',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator('^\\d{4}$', message='Enter numbers only')], verbose_name='Card Verification Value'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='code',
            field=models.CharField(max_length=3, unique=True, validators=[django.core.validators.RegexValidator('^\\d{3}$', message='Enter numbers only')], verbose_name='Code'),
        ),
    ]