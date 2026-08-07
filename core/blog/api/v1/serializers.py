from rest_framework import serializers
from ...models import Post

# Base serializers
# class PostSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=200)

# Model serializers
class PostSerializers(serializers.ModelSerializer):

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