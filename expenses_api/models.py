from django.db import models

# Create your models here.
class Expenses(models.Model):
    date = models.DateField()
    # category = models.CharField(max_length=40)
    details = models.CharField(max_length=200) 
    amount = models.IntegerField()

class Category(models.Model):
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)