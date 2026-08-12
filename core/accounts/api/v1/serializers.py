from rest_framework import serializers
from ...models import CustomUser
import django.contrib.auth.password_validation as validators
from django.core import exceptions

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