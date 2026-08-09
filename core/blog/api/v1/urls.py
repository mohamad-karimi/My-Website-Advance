from django.urls import path
from blog.api.v1.views import ListPostGenericView, DetailPostGenericView

app_name = "api-v1"

urlpatterns = [
    path("post/", ListPostGenericView.as_view(), name="post-list"),
    path('post/<int:pk>/', DetailPostGenericView.as_view(), name='post-detail'),
]