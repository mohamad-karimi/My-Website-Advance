from django.urls import path
from django.views.generic import RedirectView
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogView.as_view()),
    path("google/", RedirectView.as_view(url="https://www.google.com/"), name="go-to-google"),
    path("post/", views.PostListView.as_view(), name="list_post"),
    path("post<int:id>", views.PostDetailView.as_view(), name="single_post")
]