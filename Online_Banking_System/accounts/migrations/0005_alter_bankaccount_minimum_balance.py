# Generated by Django 4.0.3 on 2022-04-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_image_bankaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='Minimum_Balance',
            field=models.DecimalField(decimal_places=2, default=3000, max_digits=6),
        ),
    ]