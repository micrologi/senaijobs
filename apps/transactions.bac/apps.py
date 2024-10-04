from django.apps import AppConfig
from apps.transactions.models import Transaction

class TransactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.' + Transaction.tableName()
