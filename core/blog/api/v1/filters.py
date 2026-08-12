from django_filters import rest_framework as filters
from ...models import Post
from ...models import Category
from accounts.models import Profile

class PostFilter(filters.FilterSet):
    '''
    Make a custom class filter for filter the post and make the
    category and author to checkbox 
    '''
    category = filters.ModelMultipleChoiceFilter(
        field_name='category',
        queryset=Category.objects.all()
    )

    author = filters.ModelMultipleChoiceFilter(
        field_name="author",
        queryset=Profile.objects.all()
    )

    status = filters.BooleanFilter(field_name='status')

    class Meta:
        '''
        Set the model and choose the fields
        '''
        model = Post
        fields = ['category', 'author', 'status']