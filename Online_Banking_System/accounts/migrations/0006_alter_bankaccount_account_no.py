# Generated by Django 4.0.3 on 2022-04-01 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_bankaccount_minimum_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_no',
            field=models.IntegerField(unique=True),
        ),
    ]
