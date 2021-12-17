from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Bank, Account
from accounts.api.serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    """
        Bank API
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# class TransactionAPIView(APIView):
#     """
#         Transaction API
#     """
#     def get(self, request):
#         transactions = Transaction.objects.all()
#         serializer = TransactionSerializer(Transactions, many=True)

#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TransactionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)