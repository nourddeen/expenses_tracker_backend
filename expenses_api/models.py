from django.db import models

# Create your models here.
# 
class Category(models.Model):
    # expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    name = models.CharField(max_length=40 , unique=True)

class Expenses(models.Model):
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    details = models.CharField(max_length=200) 
    amount = models.IntegerField()

