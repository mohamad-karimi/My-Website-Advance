from rest_framework import serializers
from ...models import Post, Category

# Base serializers
# class PostSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=200)

# Model serializers
class PostSerializers(serializers.ModelSerializer):
    '''
    # Make serializer for post model
    '''
    class Meta:
        model = Post
        fields  = [
            "id",
            "title",
            "author",
            "content",
            "status",
            "category",
            "published_date",
        ]

class CategorySerializers(serializers.ModelSerializer):
    '''
    # Make serializer for Category
    '''
    class Meta:
        model = Category
        fields  = [
            "id",
            "name",
        ]