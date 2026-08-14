from rest_framework import serializers
from ...models import CustomUser, Profile
import django.contrib.auth.password_validation as validators
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    '''
    Serializer for registering a new user.
    Validates password confirmation and Django password requirements.
    '''

    password2 = serializers.CharField(max_length=120, write_only = True)
    class Meta():
        '''
        Define the user model and fields required for registration.
        '''
                
        model = CustomUser
        fields = [
            "email",
            "password",
            "password2",
        ]

    def validate(self, attrs):
        '''
        Validate password confirmation and password strength.
        '''
                
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
        '''
        Create a new user using the custom user manager.
        '''
                
        validated_data.pop("password2", None)

        return CustomUser.objects.create_user(**validated_data)

class CustomAuthTokenSerializer(serializers.Serializer):
    '''
    Serializer for authenticating a user with email and password.
    Checks the user's credentials and email verification status.
    '''
        
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
        '''
        Authenticate the user using the provided email and password.
        '''
                
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                username=email,
                password=password
            )

            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(
                    msg,
                    code="authorization"
                )
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(
                msg,
                code="authorization"
            )

        if not user.is_verified:
            raise serializers.ValidationError({
                "detail": "Your account is not verified."
            })

        attrs["user"] = user
        return attrs
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''
    Custom JWT serializer that adds user information to the token response
    and prevents unverified users from obtaining JWT tokens.
    '''
    
    def validate(self, attrs):
        '''
        Validate credentials and return JWT tokens with user information.
        '''
                
        validate_data = super().validate(attrs)
        validate_data["email"] = self.user.email
        validate_data["user_id"] = self.user.id

        if not self.user.is_verified:
            raise serializers.ValidationError({
                "detail": "Your account is not verified."
            })
    
        return validate_data
    
class PasswordChangeSerializer(serializers.Serializer):
    '''
    Serializer for changing the user's password.
    Validates the old password and confirms the new password.
    '''
        
    old_password = serializers.CharField(
        required=True,
        write_only=True
    )

    new_password = serializers.CharField(
        required=True,
        write_only=True
    )

    new_password2 = serializers.CharField(
        required=True,
        write_only=True
    )

    def validate(self, attrs):
        '''
        Validate that the new password and its confirmation match.
        '''
        
        if attrs["new_password"] != attrs["new_password2"]:
            raise serializers.ValidationError({
                "new_password2": "Passwords do not match."
            })

        return attrs
    
class ProfileSerializer(serializers.ModelSerializer):
    '''
    Serializer for managing additional user profile information.
    '''

    class Meta:
        '''
        Define the profile model and fields exposed through the API.
        '''
                
        model = Profile
        fields = [
            "first_name",
            "last_name",
        ]

class ActivationResendSerializer(serializers.Serializer):
    '''
    Serializer for requesting a new email activation link.
    Checks that the user exists and has not already verified their email.
    '''
        
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        '''
        Validate the user's email and check their verification status.
        '''
                
        try:
            user = User.objects.get(email=attrs["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "User with this email does not exist."})

        if user.is_verified:
            raise serializers.ValidationError({"email": "Email is already verified."})

        attrs["user"] = user
        return attrs