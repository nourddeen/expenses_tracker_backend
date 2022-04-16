from django.contrib import admin

# Register your models here.
from .models import Expenses,Category
admin.site.register(Expenses)
admin.site.register(Category)