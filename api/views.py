from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransactionSerializer

from .models import Transaction, Account

# Create your views here.
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#wrapping-api-views

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/transaction-list/',
        'List Account': '/transaction-list/?account=<str:pk>',
        'List Debit/Credito': '/transaction-list/?function=<str:function>',
        'List Account 1 and Credit': '/transaction-list/?account=1&function=<str:function>',
        'Detail': '/transaction-detail/<str:pk>',
        'Create': '/transaction-create/',
        'Update': '/transaction-update/<str:pk>',
    }

    return Response(api_urls)

@api_view(['GET'])
def transactionList(request):
    transactions = Transaction.objects.all()
    accounts = Account.objects.filter(pk__in=list({transaction.account.id for transaction in transactions}))

    if request.GET.get('account'):
        transactions = transactions.filter(account__id=request.GET.get('account'))

    if request.GET.get('function'):
        transactions = transactions.filter(function=request.GET.get('function').upper())

    serializer = TransactionSerializer(transactions, many=True)

    opening_balance = sum([account.balance for account in accounts])
    operating_balance = sum([transaction.value * -1 if transaction.function == 'D' else transaction.value for transaction in transactions])
    final_balance = opening_balance + operating_balance

    response = {
        'status': status.HTTP_200_OK,
        'message': 'Transactions',
        'response': serializer.data,
        'opening_balance': opening_balance,
        'final_balance': final_balance,
    }

    return Response(response)

@api_view(['GET'])
def transactionDetail(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(transaction, many=False)

    response = {
        'status': status.HTTP_200_OK,
        'message': 'Detail Transaction',
        'response': serializer.data,
    }

    return Response(response)

@api_view(['POST'])
def transactionCreate(request):
    serializer = TransactionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    response = {
        'status': status.HTTP_200_OK,
        'message': 'Create Transaction',
        'response': serializer.data,
    }

    return Response(response)

@api_view(['POST'])
def transactionUpdate(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(instance=transaction, data=request.data)

    if serializer.is_valid():
        serializer.save()

    response = {
        'status': status.HTTP_200_OK,
        'message': 'Update Transaction',
        'response': serializer.data,
    }

    return Response(response)