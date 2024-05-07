from django.db import models
from bankapp.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient_account_number = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    TRANSACTION_TYPES = (
        ('DEPOSIT', 'DEPOSIT'),
        ('WITHDRAWAL', 'WITHDRAWAL'),
        ('TRANSFER', 'TRANSFER'),
    )
    transaction_type = models.CharField(choices=TRANSACTION_TYPES, max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
