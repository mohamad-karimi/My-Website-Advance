from django.urls import path
from . import views

app_name = 'api-v1'

urlpatterns = [ 
    path('registration', views.RegistrationApiView.as_view(), name="registration"),
    path('token/login/', views.CustomObtainAuthToken.as_view(), name="token-login"),
    path('token/logout/', views.CustomDestroyAuthToken.as_view(), name="token-logout"),
]