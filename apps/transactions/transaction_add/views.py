from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout
from apps.transactions.models import Transaction
from apps.transactions.forms import TransactionForm
from django.contrib.auth.mixins import PermissionRequiredMixin

class TransactionAddView(PermissionRequiredMixin, TemplateView):
    permission_required = Transaction.tableName() + ".add_transaction"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        fields = Transaction._meta.get_fields()

        #Workaround pois preciso do nome com hifén no template
        for field in fields:
            field.attname = field.attname.replace('_','-')

        # Update the context
        context.update(
            {
                "fields": fields,
                "transactions_count": Transaction.objects.count(),
            }
        )
        TemplateHelper.map_context(context)

        return context

    # Post - Adiciona os dados
    def post(self, request):
        try:
            form = TransactionForm(request.POST)

            if form.is_valid():
                if not self.transaction_exists(form.cleaned_data):
                    form.save()
                    messages.success(request, "Registro adicionado")
                else:
                    messages.error(request, "Um registro semelhante já existe")
            else:
                messages.error(request, "Adição falhou")
        except BaseException as e:
            print(str(e))

        return redirect(Transaction.tableName())


    def transaction_exists(self, cleaned_data):
        return False
        """
        return Transaction.objects.filter(
            customer__iexact=cleaned_data["customer"],
            transaction_date=cleaned_data["transaction_date"],
            due_date=cleaned_data["due_date"],
            total=cleaned_data["total"],
            status=cleaned_data["status"],
        ).exists()
        """
