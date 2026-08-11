from django_filters import rest_framework as filters
from ...models import Post
from ...models import Category
from accounts.models import Profile

class PostFilter(filters.FilterSet):
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
        model = Post
        fields = ['category', 'author', 'status']