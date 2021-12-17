# Generated by Django 3.2.9 on 2021-12-17 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20211216_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.CharField(default=1, max_length=255, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='function',
            field=models.CharField(choices=[('D', 'Debit'), ('C', 'Credit')], default='D', max_length=1, verbose_name='Function'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Value'),
        ),
    ]
