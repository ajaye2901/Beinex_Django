from rest_framework import serializers
from .models import Role, User, Snippet
import django.contrib.auth.password_validation as validators

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type" : "password"})


    def validate_password(self, data) :
        validators.validate_password(password=data, user=User)
        return data
    class Meta:
        model = User
        fields = ["username","password","email","mobile_phone"]

class UserListSerializer(serializers.ModelSerializer) :
        class Meta:
            model = User
            fields = '__all__'

class SnippetCreateSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Snippet
        fields = '__all__'

class SnippetListSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Snippet
        fields = '__all__'

class SnippetUpdateSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Snippet
        fields = '__all__'

class SnippetSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Snippet
        fields = '__all__'