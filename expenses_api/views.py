from rest_framework import generics, permissions, authentication
from .serializers import ExpenseSerializer,CategorySerializer
from .models import Expense, Category

class ExpenseList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        authentication.TokenAuthentication, 
        authentication.SessionAuthentication
    ]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        authentication.TokenAuthentication, 
        authentication.SessionAuthentication
    ]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class CategoryList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        authentication.TokenAuthentication, 
        authentication.SessionAuthentication
    ]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        authentication.TokenAuthentication, 
        authentication.SessionAuthentication
    ]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)