from django.db import models


class Transaction(models.Model):
    customer = models.CharField(max_length=150, verbose_name="Cliente")
    transaction_date = models.DateField(verbose_name="Data transação")
    due_date = models.DateField(verbose_name="Data conta")
    total = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Total")
    status = models.CharField(
        max_length=20,
        choices=[("Paid", "Paid"), ("Due", "Due"), ("Canceled", "Canceled")],
        verbose_name="Situação",
    )

    def tableName():
        return "transactions"

    def __str__(self):
        return self.customer
