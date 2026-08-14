from rest_framework import serializers
from ....models import Category

# Model serializers
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