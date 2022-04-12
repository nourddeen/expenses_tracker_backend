from rest_framework import generics
from .serializers import ExpensesSerializer
from .models import Expenses

class ExpensesList(generics.ListCreateAPIView):
    queryset = Expenses.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ExpensesSerializer # tell django what serializer to use

class ExpensesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expenses.objects.all().order_by('id')
    serializer_class = ExpensesSerializer