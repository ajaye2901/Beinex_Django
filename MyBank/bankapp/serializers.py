from rest_framework import serializers
from .models import User, Customer, Account
from rest_framework_simplejwt.tokens import RefreshToken
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer


class CreateCustomerSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    mobile_number = serializers.CharField(max_length=10)
    aadhar_number = serializers.CharField(max_length=12)
    account_type = serializers.CharField(max_length=12)
    date_of_birth = serializers.DateField()
    password = serializers.CharField(max_length=16)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name','username', 'email', 'mobile_number', 'date_of_birth']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user', 'account_type', 'account_number']
        read_only_fields = ['account_number']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)  # Adding email field
    password = serializers.CharField(style={'input_type' : 'password'})

    class Meta:
        model = User
        fields = ['email', 'password']


class LoginResponseSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()
    refresh_token = serializers.SerializerMethodField()

    def get_refresh_token(self, instance):
        return str(RefreshToken.for_user(instance))

    def get_access_token(self, instance):
        return str(RefreshToken.for_user(instance).access_token)

    class Meta:
        model = User
        fields = ["user_id", "email", "first_name", "last_name", "access_token", "refresh_token"]


class CustomerDashSerializer(serializers.ModelSerializer):
    account_type = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()
    last_transactions = serializers.SerializerMethodField()
    account_number = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'account_type', 'account_number', 'balance', 'last_transactions']

    def get_account_type(self, user):
        try:
            account = Account.objects.get(customer__user=user)
            return account.account_type
        except Account.DoesNotExist:
            return None

    def get_account_number(self, user):
        try:
            return Account.objects.get(customer__user=user).account_number
        except Account.DoesNotExist:
            return None

    def get_balance(self, user):
        try:
            account = Account.objects.get(customer__user=user)
            return account.balance
        except Account.DoesNotExist:
            return None

    def get_last_transactions(self, user):
        try:
            transactions = Transaction.objects.filter(user=user).order_by('-timestamp')[:5]
            serializer = TransactionSerializer(transactions, many=True)
            return serializer.data
        except Transaction.DoesNotExist:
            return None
