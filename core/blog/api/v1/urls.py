from django.urls import path
from blog.api.v1.views import PostModelViewSet, CategoryModelViewSet
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register(r'post', PostModelViewSet, basename='post')
router.register(r'category', CategoryModelViewSet, basename='category')

urlpatterns = [
    # path("post/", ListPostGenericView.as_view(), name="post-list"),
    # path('post/<int:pk>/', DetailPostGenericView.as_view(), name='post-detail'),
#     path("post/", PostViewSet.as_view({'get': 'list', 'post':'create'}), name="post-list"),
#     path('post/<int:pk>/', PostViewSet.as_view({'get':'retrieve', 'put':'update', 'path':'partial_update', 'delete':'destroy'}), name='post-detail'),
]

urlpatterns += router.urls