from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Role, User
from .serializers import RoleSerializer, UserSerializer, UserListSerializer
from rest_framework.permissions import AllowAny

class UserCreate(CreateAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs) :
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid() :
            serializer.save()
            return Response({"message" : "Success",}, status=200)
        return Response({"message" : "Failed", "errors":serializer.errors}, status=400)
    
class UserDetails(APIView) :
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs) :
        instance = User.objects.filter(pk=kwargs.get("pk"))
        if instance.exists() :
            serializer = UserListSerializer(instance.first())
            return Response(serializer.data)
        return Response({"message" : "Failed"}, status=400)

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
