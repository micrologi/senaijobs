# Generated by Django 5.0.6 on 2024-10-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_transaction_salario'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
