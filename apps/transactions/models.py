from django.db import models
from datetime import date

class Transaction(models.Model):
    customer = models.CharField(max_length=50, verbose_name="Cliente",db_index=True)
    address = models.CharField(max_length=50, verbose_name="Endereço",db_index=False,default="")
    bairro = models.CharField(max_length=50, verbose_name="Bairro",db_index=False,default="")
    transaction_date = models.DateField(verbose_name="Data transação",db_index=True,default=date.today().strftime('%Y-%m-%d'))
    due_date = models.DateField(verbose_name="Data conta",default=date.today().strftime('%Y-%m-%d'))
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    ativo = models.BooleanField(verbose_name="Ativo",default=True)
    status = models.CharField(
        max_length=20,
        choices=[
                    ("Paid", "Paid"),
                    ("Due", "Due"),
                    ("Canceled", "Canceled")
                ],
        verbose_name="Situação",
    )

    def tableName():
        return "transactions"

    def __str__(self):
        return self.customer
