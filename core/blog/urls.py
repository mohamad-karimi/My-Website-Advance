from django.urls import path
from django.views.generic import RedirectView
from .views import BlogView

urlpatterns = [
    path("", BlogView.as_view()),
    path("google/", RedirectView.as_view(url="https://www.google.com/"), name="go-to-google")
]