from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import LoanApplication
from .serializers import LoanApplicationSerializer, LoanStatusSerializer

class ApplyLoan(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LoanApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanStatus(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        loan_applications = LoanApplication.objects.filter(user=request.user)
        print(loan_applications)
        serializer = LoanStatusSerializer(loan_applications, many=True)
        return Response(serializer.data)

