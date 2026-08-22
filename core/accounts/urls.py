from django.urls import path, include
from .views import send_email, test_delay

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    # Api V1
    path("api/v1/", include("accounts.api.v1.urls")),
    # Api V2
    # path("api/v2/", include('djoser.urls')),
    # path("api/v2/", include('djoser.urls.jwt')),
    # sending email with redis and celery
    path("sending-email/", send_email, name="sending-email"),
    path("test/delay", test_delay, name="test-delay"),
]
