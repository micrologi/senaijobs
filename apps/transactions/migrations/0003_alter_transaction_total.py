# Generated by Django 5.0.6 on 2024-10-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transaction_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total'),
        ),
    ]
