from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 
class Category(models.Model):
    name = models.CharField(max_length=40 , unique=True)
    user = models.ForeignKey(User, verbose_name = 'User', on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "categories"

class Expense(models.Model):
    date = models.DateField()
    details = models.CharField(max_length=200) 
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name = 'User', on_delete=models.CASCADE)

class Profile(models.Model):
    income = models.IntegerField(default=0, null=True)
    user = models.OneToOneField(User, verbose_name = 'User', on_delete=models.CASCADE)