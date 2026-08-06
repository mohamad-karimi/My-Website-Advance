from django.urls import path
from blog.api.v1.views import post_list, post_detail

app_name = "api-v1"

urlpatterns = [
    path("post/", post_list, name="post-list"),
    path('post/<int:id>/', post_detail, name='post-detail'),
]