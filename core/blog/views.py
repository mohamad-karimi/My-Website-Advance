from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class BlogView(TemplateView):
    '''
    Class base view to show the blog page
    '''
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Blog"
        return context