from django.urls import path, include
from .views import *


urlpatterns = [
    path('create-fixed-deposit/', CreateFixedDeposit.as_view(), name='create_fixed_deposit'),
    path('list-fixed-deposits/', ListUserFixedDeposits.as_view(), name='list_user_fixed_deposits'),
    path('deposit-calculator/', DepositCalculator.as_view(), name='deposit_calculator'),
    path('deposit-check/<int:id>', FixedDepositBalanceCheck.as_view(), name='deposit_check'),

]
