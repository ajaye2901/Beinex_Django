from django.urls import path, include
from .views import MakeTransaction, AccountToAccountTransfer


urlpatterns = [
    path('make-transaction/', MakeTransaction.as_view(), name='make_transaction'),
    path('money-transfer/', AccountToAccountTransfer.as_view(), name='money-transfer'),
]
