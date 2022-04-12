from django.db import models

# Create your models here.
class Expenses(models.Model):
    date = models.DateTimeField()
    category = models.CharField()
    details = models.CharField() 
    amount = models.IntegerField()