from rest_framework import serializers
from .models import LoanApplication
from decimal import Decimal

class LoanApplicationSerializer(serializers.ModelSerializer):
    total_amount_with_interest = serializers.SerializerMethodField()

    class Meta:
        model = LoanApplication
        fields = ['loan_type', 'amount', 'tenure', 'applied_date', 'total_amount_with_interest']

    def get_total_amount_with_interest(self, obj):
        interest_rates = {
            'personal': Decimal('0.02'), 
            'home': Decimal('0.015'),    
            'car': Decimal('0.025'),      
            'education': Decimal('0.01')  
        }

        interest_rate = interest_rates.get(obj.loan_type, Decimal('0')) 
        total_interest = obj.amount * interest_rate * Decimal(obj.tenure)
        total_amount = obj.amount + total_interest
        return total_amount
    
class LoanStatusSerializer(serializers.ModelSerializer) :
    class Meta :
        model = LoanApplication
        fields = '__all__'