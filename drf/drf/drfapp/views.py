from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Role, User, Snippet
from .serializers import RoleSerializer, UserSerializer, UserListSerializer, SnippetCreateSerializer, SnippetListSerializer, SnippetUpdateSerializer, SnippetSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .pagination import *
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter


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

class SnippetCreate(CreateAPIView) :
    queryset = Snippet.objects.all()
    serializer_class = SnippetCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs) :
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid() :
            serializer.save()
            return Response({"message" : "Success",}, status=200)
        return Response({"message" : "Failed", "errors":serializer.errors}, status=400)
    
class SnippetView(APIView) :
        permission_classes = [AllowAny]
        def get(self, *args, **kwargs) :
            instance = Snippet.objects.filter(pk=kwargs.get("pk"))
            if instance.exists() :
                serializer = SnippetListSerializer(instance.first())
                return Response(serializer.data)
            return Response({"message" : "Failed"}, status=400)
        
class SnippetUpdate(UpdateAPIView) :
    queryset = Snippet.objects.all()
    serializer_class = SnippetUpdateSerializer
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs) :
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Success",}, status=200)
        return Response({"message" : "Failed", "errors":serializer.errors}, status=400)

class SnippetDelete(DestroyAPIView) :
    queryset = Snippet.objects.all()
    serializer_class = SnippetCreateSerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try :
            self.perform_destroy(instance)
        except Exception as e :
            return Response({"message" : "Failed", "error" : str(e)}, status=400)
        return Response({"message": "Snippet deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class SnippetBulkDelete(APIView) :
    permission_classes = [AllowAny]
    def post(self, request) :
        data = request.data
        obj = data.get("obj")
        try :
            snippet_obj = Snippet.objects.filter(pk__in=obj).delete()
        except Exception as e :
            return Response({"message" : "Failed", "error" : str(e)}, status=400)
        return Response({"message" : "Success",}, status=200)
    

class SnippetList(ListAPIView) :
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    pagination_class=CustomLimitOffsetPaginations
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['text', 'snippet_id']
    ordering_fields = ['snippet_id'] 

    def get_queryset(self):
        q = self.request.GET.get('q')
        user_id = self.request.GET.get('user_id')
        snippet_id = self.request.GET.get('snippet_id')
        queryset = Snippet.objects.all()
        if q:
            queryset = Snippet.objects.filter(Q(text__icontains=q) | Q(snippet_id__icontains=q))
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if snippet_id:
            queryset = queryset.filter(snippet_id=snippet_id)

        order_by = self.request.query_params.get('order_by')
        if order_by == 'snippet_id':
            queryset = queryset.order_by('snippet_id')
        elif order_by == '-snippet_id':
            queryset = queryset.order_by('-snippet_id')
        return queryset
