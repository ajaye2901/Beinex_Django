from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import AccountSerializer, UserSerializer, CreateCustomerSerializer, LoginSerializer, LoginResponseSerializer, CustomerDashSerializer
from .models import User, Customer, Account
from transaction.serializers import TransactionSerializer
from transaction.models import Transaction
from .pagination import CustomPagination
from django.utils import timezone
import random
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group



class Customer_create(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        if not request.user.has_perm('user.add_account'):
            return Response({"message": "User does not have the required permission"}, status=status.HTTP_200_OK)
        serializer = CreateCustomerSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data['first_name']
            password = serializer.validated_data['password'] 

            user_obj = User.objects.create(
                first_name=first_name,
                last_name=serializer.validated_data['last_name'],
                email=serializer.validated_data['email'],  
                username=serializer.validated_data['email'],  
                mobile_number=serializer.validated_data['mobile_number'],
                date_of_birth=serializer.validated_data['date_of_birth'],
                password=make_password(password)  
            )

            try:
                group_obj = Group.objects.get(name='customer')
            except:
                return Response({"error": "Customer group does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            user_obj.groups.add(group_obj)

            customer_obj = Customer.objects.create(
                user=user_obj,
                aadhar_number=serializer.validated_data['aadhar_number'],
            )

            account_number = f"{user_obj.user_id:06d}{random.randint(100000, 999999)}"
            
            Account.objects.create(
                customer=customer_obj,
                account_type=serializer.validated_data['account_type'],
                account_number=account_number
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewCustomerDetails(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class Login(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                user_obj = User.objects.get(email__iexact=data["email"])
                if (data['password'], user_obj.password):
                    user_obj.last_login = timezone.now()
                    user_obj.save()
                    resp = LoginResponseSerializer(instance=user_obj)
                    resp_data = resp.data
                    return Response(resp_data, status=status.HTTP_200_OK)
                else:
                    return Response(
                        {"message": "Invalid credentials", "status": "1"},
                        status=status.HTTP_401_UNAUTHORIZED
                    )
            except User.DoesNotExist:
                return Response({"message": "Invalid user", "status": "1"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDash(RetrieveAPIView):
    serializer_class = CustomerDashSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ViewAccountStatement(ListAPIView):
    serializer_class = TransactionSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        queryset = Transaction.objects.filter(user=user).order_by('-timestamp')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
