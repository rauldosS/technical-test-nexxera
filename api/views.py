from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransactionSerializer

from .models import Transaction

# Create your views here.
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#wrapping-api-views

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/transaction-list/',
        'Detail View': '/transaction-detail/<str:pk>',
        'Create': '/transaction-create/',
        'Update': '/transaction-update/<str:pk>',
        'Delete': '/transaction-delete/<str:pk>',
    }

    return Response(api_urls)

@api_view(['GET'])
def transactionList(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def transactionDetail(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(transaction, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def transactionCreate(request):
    serializer = TransactionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def transactionUpdate(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(instance=transaction, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)