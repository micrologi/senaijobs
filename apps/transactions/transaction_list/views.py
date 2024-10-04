from django.views.generic import TemplateView
from django.db.models import Sum
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout
from apps.transactions.models import Transaction


class TransactionListView(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        transactions = self.get_annotated_transactions()

        titles = []
        fields = []
        for field in Transaction._meta.get_fields():
            titles.append(field.verbose_name)
            fields.append(field.name)

        # Update the context
        context.update(
            {
                "transactions": transactions,
                "titles": titles,
                "fields": fields,
                "transactions_count": Transaction.objects.count(),
            }
        )
        TemplateHelper.map_context(context)
        return context

    def get_annotated_transactions(self):
        # Get all transactions and order them by ID
        first_field = Transaction._meta.get_fields(
            include_parents=False, include_hidden=False
        )
        return Transaction.objects.all().order_by(first_field[0].name)

    """
    def get_total_due(self):
        total_due_amount = Transaction.objects.filter(status="Due").aggregate(
            total_due=Sum("total")
        )
        return (
            float(total_due_amount["total_due"])
            if total_due_amount["total_due"] is not None
            else 0.0
        )

    def get_total_paid(self):
        # Calculate the total sum of 'total' field for 'Paid' transactions
        total_paid_amount = Transaction.objects.filter(status="Paid").aggregate(
            total_paid=Sum("total")
        )
        return (
            float(total_paid_amount["total_paid"])
            if total_paid_amount["total_paid"] is not None
            else 0.0
        )

    def get_total_canceled(self):
        total_canceled_amount = Transaction.objects.filter(status="Canceled").aggregate(
            total_canceled=Sum("total")
        )
        return (
            float(total_canceled_amount["total_canceled"])
            if total_canceled_amount["total_canceled"] is not None
            else 0.0
        )
    """
