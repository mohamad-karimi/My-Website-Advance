from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

app_name = 'api-v1'

urlpatterns = [ 

    path('registration', views.RegistrationApiView.as_view(), name="registration"),

    path('token/login/', views.CustomObtainAuthToken.as_view(), name="token-login"),
    path('token/logout/', views.CustomDestroyAuthToken.as_view(), name="token-logout"),

    path('token/create/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]