# Generated by Django 4.0 on 2021-12-17 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_account_cvv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='limit',
        ),
    ]
