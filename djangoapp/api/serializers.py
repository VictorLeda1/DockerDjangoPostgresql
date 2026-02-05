from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'user_permissions', 'is_authenticated', 'get_full_name', 'orders')
        # exclude = ('password', 'user_permissions')
        # fields = '__all__'