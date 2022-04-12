from rest_framework import serializers 
from .models import Expenses 

class ExpensesSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Expenses # tell django which model to use
        fields = ('id', 'date', 'catagory','details','amount',) # tell django which fields to include