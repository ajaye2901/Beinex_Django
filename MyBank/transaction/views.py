from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
from .models import Transaction
from bankapp.models import Account
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated


class MakeTransaction(CreateAPIView):
    serializer_class = TransactionSerializer

    def post(self, request):
        user = request.user
        amount = Decimal(request.data.get('amount'))
        transaction_type = request.data.get('transaction_type')

        if transaction_type not in ['DEPOSIT', 'WITHDRAWAL']:
            return Response({'error': 'Invalid transaction type'}, status=status.HTTP_400_BAD_REQUEST)

        if transaction_type == 'WITHDRAWAL':
            amount = -amount

        transaction = Transaction.objects.create(user=user, amount=amount, transaction_type=transaction_type)

        account = Account.objects.get(customer__user=user)
        account.balance += amount
        account.save()
        transaction.balance = account.balance
        transaction.save()

        return Response({'message': 'Transaction created successfully'}, status=status.HTTP_201_CREATED)


class AccountToAccountTransfer(CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        recipient_account_number = request.data.get('recipient_account_number')
        amount = Decimal(request.data.get('amount'))

        try:
            recipient_account = Account.objects.get(account_number=recipient_account_number)
        except Account.DoesNotExist:
            return Response({'error': 'Recipient account not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            sender_account = Account.objects.get(customer__user=user)
        except Account.DoesNotExist:
            return Response({'error': 'Sender account not found'}, status=status.HTTP_404_NOT_FOUND)

        withdrawal_transaction = Transaction.objects.create(
            user=user,
            recipient_account_number=recipient_account_number,
            amount=-amount,
            transaction_type='TRANSFER',
        )

        deposit_transaction = Transaction.objects.create(
            user=recipient_account.customer.user,
            recipient_account_number=sender_account.account_number,
            amount=amount,
            transaction_type='TRANSFER',
        )

        sender_account.balance -= amount
        sender_account.save()
        withdrawal_transaction.balance = sender_account.balance
        withdrawal_transaction.save()

        recipient_account.balance += amount
        recipient_account.save()
        deposit_transaction.balance = recipient_account.balance
        deposit_transaction.save()

        return Response({'message': 'Transfer successful'}, status=status.HTTP_201_CREATED)
