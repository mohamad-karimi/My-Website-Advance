from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    # Api V1
    path("api/v1/", include("accounts.api.v1.urls")),

    # Api V2
    # path("api/v2/", include('djoser.urls')),
    # path("api/v2/", include('djoser.urls.jwt')),
]