from django.db import models
from bankapp.models import User

FIXED_INTEREST_RATE = 6

class FixedDeposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    principal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tenure_months = models.PositiveIntegerField()
    maturity_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)

    def calculate_maturity_amount(self):
        interest_amount = (self.principal_amount * FIXED_INTEREST_RATE * self.tenure_months) / 100
        self.maturity_amount = self.principal_amount + interest_amount
        self.save()