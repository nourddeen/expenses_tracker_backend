from rest_framework import serializers 
from .models import Expenses, Category

# class ExpensesSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
#     class Meta:
#         model = Expenses # tell django which model to use
#         fields = ('id', 'date','category','details','amount',) # tell django which fields to include

class ExpensesSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Expenses # tell django which model to use
        fields = ('id', 'date','details','amount',) # tell django which fields to include

class CategorySerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Category # tell django which model to use
        fields = ('id', 'name','expense') # tell django which fields to include