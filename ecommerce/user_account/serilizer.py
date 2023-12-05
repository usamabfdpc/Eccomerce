from rest_framework import serializers
from .models import User


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','is_verified']


class VarifyAccountSerilizer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()