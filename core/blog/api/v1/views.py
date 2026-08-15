from ...models import Post, Category
from .serializers import PostSerializers, CategorySerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .permissions import IsOwnerOrAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import CustomPagination
from .filters import PostFilter

# Example for function base view
'''
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

    """
    FBV for getting and update and delete each post
    """
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

# Example for class base view
"""
    '''
    CBV for getting and creating list of posts
    '''
    class ListPostApiView(APIView):
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
    class DetailPostApiView(APIView):
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
"""

# Example for generic view
"""
    class ListPostGenericView(ListCreateAPIView):
        '''
        Use list and create GAV for show the list of
        the post and create a new post
        '''
        permission_classes = [IsAuthenticated]
        serializer_class = PostSerializers

        queryset = Post.objects.filter(status=True)

    class DetailPostGenericView(RetrieveUpdateDestroyAPIView):
        '''
        Use retrieve, update and destroy for show a detail info and update and 
        delete the post
        '''
        permission_classes = [IsAuthenticated]
        serializer_class = PostSerializers

        queryset = Post.objects.filter(status=True)
"""

# Example for View sets
"""
    class PostViewSet(viewsets.ViewSet):
        '''
        use view set for blog post
        '''
        permission_classes = [IsAuthenticated]
        serializer_class = PostSerializers

        queryset = Post.objects.filter(status=True)

        def list(self, request):
            '''
            show the list of the post
            '''
            serializer = self.serializer_class(self.queryset, many=True)
            return Response(serializer.data)
        
        def retrieve(self, request, pk=None):
            '''
            Filter the post with id to show the detail of the
            each post
            '''
            post = get_object_or_404(self.queryset, pk=pk)
            serializer = self.serializer_class(post)
            return Response(serializer.data)
        
        def create(self, request):
            pass

        def update(self, request, pk=None):
            pass

        def partial_update(self, request, pk=None):
            pass

        def destroy(self, request, pk=None):
            pass
"""


# Example for model view Set
class PostModelViewSet(viewsets.ModelViewSet):
    """
    use model view set for blog post to show list of the post and details
    post and create, pull, path, delete
    """

    permission_classes = [
        IsOwnerOrAdminOrReadOnly,
    ]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = CustomPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    """
    use model view set for blog post to show list of the post and details
    post and create, pull, path, delete
    """

    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
