from datetime import date
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import FixedDeposit
from .serializers import FixedDepositSerializer, FixedDepositAmountSerializer, FixedDepositBalanceCheckSerializer

class CreateFixedDeposit(CreateAPIView):
    queryset = FixedDeposit.objects.all()
    serializer_class = FixedDepositSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListUserFixedDeposits(ListAPIView):
    serializer_class = FixedDepositSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FixedDeposit.objects.filter(user=self.request.user)


class DepositCalculator(ListAPIView):
    serializer_class = FixedDepositAmountSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FixedDepositAmountSerializer(data=request.data)
        if serializer.is_valid():
            total_amount = serializer.calculate_total_amount(serializer.validated_data)
            return Response({'total_amount': total_amount}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class FixedDepositBalanceCheck(RetrieveAPIView):
    serializer_class = FixedDepositBalanceCheckSerializer
    queryset = FixedDeposit.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            instance = FixedDeposit.objects.get(id=kwargs.get("id"))
            print(instance)
            if instance:
                current_date = date.today()  
                serializer = self.get_serializer(data={'fixed_deposit_id': instance.id, 'current_date': current_date})
                serializer.is_valid(raise_exception=True)
                print(serializer.validated_data)
                matured_amount = serializer.calculate_matured_amount(serializer.validated_data)
                return Response({'matured_amount': matured_amount}, status=status.HTTP_200_OK)
        except FixedDeposit.DoesNotExist:
            return Response({"message": "Fixed deposit not found"}, status=status.HTTP_404_NOT_FOUND)