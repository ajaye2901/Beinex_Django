from decimal import Decimal
from rest_framework import serializers
from .models import Transaction
from django.utils import timezone

class TransactionSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", default_timezone=timezone.get_current_timezone())

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'timestamp']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['transaction_type'] == 'WITHDRAWAL':
            data['amount'] = abs(Decimal(data['amount']))
        return data
