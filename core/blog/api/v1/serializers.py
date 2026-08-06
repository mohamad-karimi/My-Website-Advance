from rest_framework import serializers

class PostSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=200)