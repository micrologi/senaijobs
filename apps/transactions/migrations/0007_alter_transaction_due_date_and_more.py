# Generated by Django 5.0.6 on 2024-10-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_transaction_ativo_alter_transaction_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='due_date',
            field=models.DateField(default='2024-10-08', verbose_name='Data conta'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateField(db_index=True, default='2024-10-08', verbose_name='Data transação'),
        ),
    ]
