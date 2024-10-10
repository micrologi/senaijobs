from django.db import models
from datetime import date

class Transaction(models.Model):
    empresa = models.CharField(verbose_name="Empresa", max_length=50, db_index=True,default="")
    atividades = models.CharField(verbose_name="Atividades", max_length=100, db_index=False,default="")
    requisitos = models.CharField(verbose_name="Requisitos", max_length=100, db_index=False,default="")
    contato = models.CharField(verbose_name="Contato", max_length=50, db_index=False,default="")
    area = models.IntegerField(verbose_name="Área",
        choices=[
                    (1, "Administração e gestão"),
                    (2, "Alimentos e bebidas"),
                    (3, "Construção civil e design"),
                    (4, "Moda Têxtil, calçados e joalheria"),
                    (5, "Papel, celulose, gráfica, editorial"),
                    (6, "Mecânica industrial"),
                    (7, "Logistica e transporte"),
                    (8, "Automotiva"),
                    (9, "Mecâtronica, automação e energia"),
                    (10, "Meio ambiente, saúde e segurança do trabalho"),
                    (11, "Metalurgia e soldagem"),
                    (12, "Química cerâmica e plásticos"),
                    (13, "Refrigeração e climatização"),
                    (14, "Tecnologia da informação"),
                    (15, "Outras")
                ],default=15
    )
    salario = models.DecimalField(verbose_name="Salário", max_digits=10, decimal_places=2, default=0)
    aprovada = models.BooleanField(verbose_name="Aprovada",default=False)

    '''
    data_transacao = models.DateField(verbose_name="Data transação",db_index=True,default=date.today().strftime('%Y-%m-%d'))
    due_date = models.DateField(verbose_name="Data conta",default=date.today().strftime('%Y-%m-%d'))
    total = models.DecimalField(verbose_name="Total",max_digits=10, decimal_places=2)
    status = models.CharField(verbose_name="Situação",
        max_length=20,
        choices=[
                    ("Paid", "Paid"),
                    ("Due", "Due"),
                    ("Canceled", "Canceled")
                ]
    )
    '''

    def tableName():
        return "transactions"

    def __str__(self):
        return self.id
