# Generated by Django 4.0.3 on 2022-03-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleetManagement', '0004_alter_contract_contract_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_end_date',
            field=models.DateField(),
        ),
    ]
