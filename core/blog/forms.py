from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    '''
    This class for set the fields of the post form
    '''
    class Meta:
        model = Post
        fields = (
            "title",
            "image",
            "content",
            "category",
            "published_date",
        )