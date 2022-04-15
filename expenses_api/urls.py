from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExpensesList.as_view(), name='Expenes_list'), # api/contacts will be routed to the ContactList view for handling
    path('/<int:pk>', views.ExpensesDetail.as_view(), name='Expenses_detail'), # api/contacts will be routed to the ContactDetail view for handling
]