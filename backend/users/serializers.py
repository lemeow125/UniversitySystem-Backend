from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from users.models import CustomUser
import secrets

def make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789&#$!@()*^><?/[]'):
    return ''.join(secrets.choice(allowed_chars) for i in range(length))

userfields = ('first_name','last_name','email')
userfields_readonly = ('id','is_banned','is_superuser','is_staff','is_student')

class CustomUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = CustomUser
        fields = userfields
        read_only_fields = userfields_readonly


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = CustomUser 
        fields = userfields

    def create(self,validated_data):
        user = self.Meta.model(**validated_data)
        user.set_password(make_random_password())
        
        return user.save()
