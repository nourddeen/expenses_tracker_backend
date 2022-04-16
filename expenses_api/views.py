from rest_framework import generics
from .serializers import ExpensesSerializer,CategorySerializer
from .models import Expenses, Category

class ExpensesList(generics.ListCreateAPIView):
    queryset = Expenses.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ExpensesSerializer # tell django what serializer to use

class ExpensesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expenses.objects.all().order_by('id')
    serializer_class = ExpensesSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = CategorySerializer # tell django what serializer to use

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


