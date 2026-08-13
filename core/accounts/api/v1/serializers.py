from rest_framework import serializers
from ...models import CustomUser
import django.contrib.auth.password_validation as validators
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=120, write_only = True)
    class Meta():
        model = CustomUser
        fields = [
            "email",
            "password",
            "password2",
        ]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError(
                {
                    "detail":"passwords not match"
                }
            )
        
        try:
             validators.validate_password(password=attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return attrs
    
    def create(self, validated_data):
        validated_data.pop("password2", None)

        return CustomUser.objects.create_user(**validated_data)

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )

    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                username=email,
                password=password
            )

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(
                    msg,
                    code='authorization'
                )
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(
                msg,
                code='authorization'
            )

        attrs['user'] = user
        return attrs
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        validate_date = super().validate(attrs)
        validate_date["email"] = self.user.email
        validate_date["user_id"] = self.user.id

        return validate_date