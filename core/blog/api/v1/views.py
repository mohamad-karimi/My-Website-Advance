from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import Post
from .serializers import PostSerializers
from rest_framework import status

@api_view(["GET", "POST"])
def post_list(request):
    if request.method == "GET":
        post = Post.objects.filter(status=True)
        serializers = PostSerializers(post, many=True)
        return Response(serializers.data)
    if request.method == "POST":
        serializers = PostSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, id):
    try:
        post = Post.objects.get(pk = id, status=True)
    except Post.DoesNotExist:
        return Response({"detail":"Post not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializers = PostSerializers(post)
        return Response(serializers.data)
    
    elif request.method == "PUT":
        serializers = PostSerializers(post, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"Post deleted"}, status=status.HTTP_204_NO_CONTENT)