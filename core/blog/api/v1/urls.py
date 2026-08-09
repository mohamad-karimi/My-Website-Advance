from django.urls import path
from blog.api.v1.views import ListPost, DetailPost

app_name = "api-v1"

urlpatterns = [
    path("post/", ListPost.as_view(), name="post-list"),
    path('post/<int:id>/', DetailPost.as_view(), name='post-detail'),
]