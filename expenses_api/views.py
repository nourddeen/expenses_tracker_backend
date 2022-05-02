from rest_framework import generics, permissions, authentication
from .serializers import ExpenseSerializer,CategorySerializer, ProfileSerializer
from .models import Expense, Category, Profile



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
        params = self.request.query_params

        queryset = Expense.objects.filter(user_id=self.request.user.id)
        if params.get('from_date', None) is not None and params.get('to_date', None) is not None:
            queryset = queryset.filter(date__range=(params['from_date'], params['to_date']))

        if params.get('from_date', None) is not None and params.get('to_date', None) is None:
            queryset = queryset.filter(date__gte=params['from_date'])

        if params.get('to_date', None) is not None and params.get('from_date', None) is None:
            queryset = queryset.filter(date__lte=params['to_date'])

        return queryset

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

class ProfileList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        authentication.TokenAuthentication, 
        authentication.SessionAuthentication
    ]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        authentication.TokenAuthentication, 
        authentication.SessionAuthentication
    ]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
