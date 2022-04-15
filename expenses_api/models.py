from django.db import models

# Create your models here.
class Expenses(models.Model):
    date = models.DateTimeField()
    category = models.CharField(max_length=40)
    details = models.CharField(max_length=200) 
    amount = models.IntegerField()