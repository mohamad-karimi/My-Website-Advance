from rest_framework import serializers
from ...models import Post
from django.urls import reverse
from accounts.models import Profile

# Base serializers
'''
    class PostSerializers(serializers.Serializer):
        title = serializers.CharField(max_length=200)
'''

class PostSerializers(serializers.ModelSerializer):
    '''
    # Make serializer for post model
    '''
    snippet = serializers.ReadOnlyField(source='get_snippet')
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        read_only_fields = ["author"]
        model = Post
        fields  = [
            "id",
            "title",
            "image",
            "absolute_url",
            "author",
            "content",
            "snippet",
            "status",
            "category",
            "published_date",
        ]

    def get_absolute_url(self, obj):
        '''
        Make url for each post
        '''
        request = self.context.get("request")
        url = reverse("blog:api-v1:post-detail", kwargs={"pk": obj.pk})

        if request:
            return request.build_absolute_uri(url)

        return url
    
    def to_representation(self, instance):
        '''
        Change the category show and change the feature to
        show in the just in the single or list
        '''
        rep =  super().to_representation(instance)
        request = self.context.get("request")

        rep["category"] = CategorySerializers(instance.category, context={"request":request}).data
        
        if request and request.resolver_match:
            if request.resolver_match.url_name == "post-detail":
                rep.pop("absolute_url", None)
            if request.resolver_match.url_name == "post-list":
                rep.pop("content")

        return rep
    
    def create(self, validated_data):
        '''
        Get the id user and find the profile that user is
        make that post and use it in the author field
        '''
        validated_data["author"] = Profile.objects.get(user__id = self.context.get("request").user.id)
        return super().create(validated_data)