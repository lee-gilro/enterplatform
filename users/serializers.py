from django.forms import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import User

class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "gender",
            "avatar",
            "username",
            
        )

class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "is_staff",
            "id",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
            "point",

        )

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("이미 존재하는 이메일 주소입니다.")
        return value

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['email'],  # username을 email과 동일하게 설정

        )
        user.set_password(validated_data['password'])
        user.save()
        return user