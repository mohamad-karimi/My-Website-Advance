from rest_framework.generics import GenericAPIView
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from ...models import Profile
from django.shortcuts import get_object_or_404

User = get_user_model

@extend_schema(tags=["Authentication"])
class RegistrationApiView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                "email":serializer.validated_data["email"]
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@extend_schema(tags=["Token"])
class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs): 
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

@extend_schema(tags=["Token"])
class CustomDestroyAuthToken(APIView):

    def post(self, request):
        request.user.auth_token.delete()

        return Response(status=status.HTTP_204_NO_CONTENT) 
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@extend_schema(tags=["Authentication"])
class PasswordChangeApiView(GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        user = self.get_object()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not user.check_password(
            serializer.validated_data["old_password"]
        ):
            return Response(
                {"old_password": ["Wrong password."]},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(
            serializer.validated_data["new_password"]
        )
        user.save()

        return Response(
            {"detail": "Password changed successfully."},
            status=status.HTTP_200_OK
        )

@extend_schema(tags=["Profile"])
class ProfileApiView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj