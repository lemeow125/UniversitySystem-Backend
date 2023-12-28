from djoser.serializers import UserSerializer as BaseUserSerializer
from drf_extra_fields.fields import HybridImageField

from rest_framework import serializers
from users.models import CustomUser
import secrets


def make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789&#$!@()*^><?/[]'):
    return ''.join(secrets.choice(allowed_chars) for i in range(length))


class CustomUserSerializer(BaseUserSerializer):
    avatar = HybridImageField(required=False)

    class Meta(BaseUserSerializer.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'avatar')
        read_only_fields = ('id', 'is_banned', 'is_superuser',
                            'is_staff', 'is_student')


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')
