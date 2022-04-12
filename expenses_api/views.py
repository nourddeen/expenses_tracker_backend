from rest_framework import generics
from .serializers import ExpensesSerializer
from .models import Contact

class ExpensesList(generics.ListCreateAPIView):
    queryset = Contact.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ExpensesSerializer # tell django what serializer to use

class ExpensesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ExpensesSerializer