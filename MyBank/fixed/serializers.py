from datetime import datetime
from decimal import Decimal
from rest_framework import serializers
from .models import FixedDeposit, FIXED_INTEREST_RATE


class FixedDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedDeposit
        fields = ['principal_amount','tenure_months']

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.calculate_maturity_amount()
        return instance
    

class FixedDepositAmountSerializer(serializers.Serializer):
    principal_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    tenure_months = serializers.IntegerField(min_value=1)

    def validate_tenure_months(self, value):
        if value % 12 != 0:
            raise serializers.ValidationError("Tenure should be in multiples of 12 months.")
        return value

    def calculate_total_amount(self, validated_data):
        principal_amount = validated_data['principal_amount']
        tenure_months = validated_data['tenure_months']
        monthly_interest_rate = Decimal(str(FIXED_INTEREST_RATE)) / 12 / 100
        total_amount = principal_amount + (principal_amount * monthly_interest_rate * tenure_months)
        return total_amount
    

class FixedDepositBalanceCheckSerializer(serializers.Serializer):
    fixed_deposit_id = serializers.IntegerField(required=True)
    current_date = serializers.DateField()

    def validate_fixed_deposit_id(self, value):
        try:
            fixed_deposit = FixedDeposit.objects.get(id=value)
        except FixedDeposit.DoesNotExist:
            raise serializers.ValidationError("Fixed deposit not found")
        return value


    def calculate_matured_amount(self, validated_data):
        fixed_deposit_id = validated_data['fixed_deposit_id']
        current_date = validated_data['current_date']
        fixed_deposit = FixedDeposit.objects.get(id=fixed_deposit_id)
        principal_amount = fixed_deposit.principal_amount
        tenure_months = fixed_deposit.tenure_months
        start_date = fixed_deposit.start_date
        print(current_date.year)
        elapsed_months = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)
        monthly_interest_rate = Decimal(str(FIXED_INTEREST_RATE)) / 12 / 100
        matured_amount = principal_amount + (principal_amount * monthly_interest_rate * elapsed_months)

        return matured_amount