import sys
import os
from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.transactions.models import Transaction

sys.path.insert(0,os.getcwd() + "\\apps\\" + Transaction.tableName() + "\\" )

from transaction_list.views import TransactionListView
from transaction_add.views import TransactionAddView
from transaction_update.views import TransactionUpdateView
from transaction_delete.views import TransactionDeleteView

urlpatterns = [
    path(
        Transaction.tableName() + "/list/",
        login_required(TransactionListView.as_view(template_name=Transaction.tableName()+"_list.html")),
        name=Transaction.tableName(),
    ),
    path(
        Transaction.tableName()+"/add/",
        login_required(TransactionAddView.as_view(template_name=Transaction.tableName()+"_add.html")),
        name=Transaction.tableName()+"-add",
    ),
    path (
        Transaction.tableName()+"/update/<int:pk>",
        login_required(TransactionUpdateView.as_view(template_name=Transaction.tableName()+"_update.html")),
        name=Transaction.tableName()+"-update",
    ),
    path (
        Transaction.tableName()+"/delete/<int:pk>/",
        login_required(TransactionDeleteView.as_view()),
        name=Transaction.tableName()+"-delete",
    ),

]
