from django.urls import path
from . import views

urlpatterns = [
    path('api/expenses', views.ExpenseList.as_view(), name='Expense_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/expenses/<int:pk>', views.ExpenseDetail.as_view(), name='Expense_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('api/category', views.CategoryList.as_view(), name='Category_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/category/<int:pk>', views.CategoryDetail.as_view(), name='Category_detail'), # api/contacts will be routed to the ContactDetail view for handling
]