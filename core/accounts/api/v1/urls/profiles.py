from django.urls import path
from .. import views

app_name = 'api-v1'

urlpatterns = [ 
    path('', views.ProfileApiView.as_view(), name="profile"),
]