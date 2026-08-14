from django.urls import path
from .. import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [ 
    # Registration
    path('registration', views.RegistrationApiView.as_view(), name="registration"),

    # Activation
    path("activation/confirm/<str:token>", views.ActivationConfirmApiView.as_view(), name="activation-confirm"),
    
    # Reset Activation
    path("activation/resend/", views.ActivationResendApiView.as_view(), name="activation-resend"),

    # Change password
    path('password/change/', views.PasswordChangeApiView.as_view(), name="password-change"),

    # Token login
    path('token/login/', views.CustomObtainAuthToken.as_view(), name="token-login"),
    path('token/logout/', views.CustomDestroyAuthToken.as_view(), name="token-logout"),

    # Jwt login
    path('token/create/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]