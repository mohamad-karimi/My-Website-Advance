from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import Post
from .serializers import PostSerializers
from rest_framework import status

@api_view()
def post_list(request):
    post = Post.objects.filter(status=True)
    serializers = PostSerializers(post, many=True)
    return Response(serializers.data)

@api_view()
def post_detail(request, id):
    try:
        post = Post.objects.get(pk = id, status=True)
        serializers = PostSerializers(post)
        return Response(serializers.data)
    except Post.DoesNotExist:
        return Response({"detail":"Post not found"}, status=status.HTTP_404_NOT_FOUND)
