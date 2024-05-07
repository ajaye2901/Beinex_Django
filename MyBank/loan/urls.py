from django.urls import path
from loan.views import ApplyLoan, LoanStatus

urlpatterns = [
    path('apply-loan/', ApplyLoan.as_view(), name='apply_loan'),
    path('loan-status/', LoanStatus.as_view(), name='loan_status'),
]
