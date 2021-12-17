from django.urls import include, path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('transaction-list/', views.transactionList, name='transaction-list'),
    path('transaction-detail/<str:pk>', views.transactionDetail, name='transaction-detail'),
    path('transaction-create', views.transactionCreate, name='transaction-create'),
    path('transaction-update/<str:pk>', views.transactionUpdate, name='transaction-update'),
]