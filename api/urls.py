from django.urls import include, path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('transactions/', views.transactionList, name='transaction-list'),
    path('transactions/<str:pk>', views.transactionDetail, name='transaction-detail'),
    path('transactions', views.transactionCreate, name='transaction-create'),
    path('transaction/<str:pk>', views.transactionUpdate, name='transaction-update'),
]