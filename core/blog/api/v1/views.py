from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ...models import Post
from .serializers import PostSerializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

"""
FBV for getting and creating list of posts
"""
# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
# def post_list(request):
    # if request.method == "GET":
    #     post = Post.objects.filter(status=True)
    #     serializers = PostSerializers(post, many=True)
    #     return Response(serializers.data)
    # if request.method == "POST":
    #     serializers = PostSerializers(data=request.data)
    #     serializers.is_valid(raise_exception=True)
    #     serializers.save()
    #     return Response(serializers.data)

'''
FBV for getting and update and delete each post
'''
# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def post_detail(request, id):
#     try:
#         post = Post.objects.get(pk = id, status=True)
#     except Post.DoesNotExist:
#         return Response({"detail":"Post not found"}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializers = PostSerializers(post)
#         return Response(serializers.data)
    
#     elif request.method == "PUT":
#         serializers = PostSerializers(post, data=request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response(serializers.data)
    
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail":"Post deleted"}, status=status.HTTP_204_NO_CONTENT)
    
    
'''
CBV for getting and creating list of posts
'''
class ListPost(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers

    def get(self,request):
        '''
        Getting data for show the list of posts
        '''
        post = Post.objects.filter(status=True)
        serializers = PostSerializers(post, many=True)
        return Response(serializers.data)
    
    def post(self,request):
        '''
        Creating a new post
        '''
        serializers = PostSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

'''
CBV for getting and update and delete each post
'''
class DetailPost(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    
    def get(self,request, id):
        '''
        Getting the detail of post
        '''
        post = get_object_or_404(Post, pk=id, status=True)
        serializers = self.serializer_class(post)
        return Response(serializers.data)
    
    def put(self,request,id):
        '''
        Updating the details info of post
        '''
        post = get_object_or_404(Post, pk=id, status=True)
        serializers = self.serializer_class(post, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    
    def delete(self, request, id):
        '''
        Deleting the post
        '''
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail":"Post deleted"}, status=status.HTTP_204_NO_CONTENT)