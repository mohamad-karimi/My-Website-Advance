from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from blog.forms import PostForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
class BlogView(TemplateView):
    '''
    Class base view to show the blog page
    '''

    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Blog"
        return context
    
    """dispatch"""
    """get_queryset"""
    
class PostListView(ListView):
    '''
    Class for list view of the posts
    '''
    # model = Post
    # template_name = "blog/post_list.html"
    # ordering = "-id"
    context_object_name = "posts"
    paginate_by = 2
    
    '''
    Filter the post that are have  true status
    '''
    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts
    
class PostDetailView(DetailView):
    '''
    class for detail view of each post
    '''
    model = Post
    context_object_name = "post"
    template_name = "blog/post_Detail.html"
    pk_url_kwarg = "id"
    # slug_url_kwarg = "slug"
    # query_pk_and_slug = "id and slug"
    
    '''
    Get post with thier id and filter them with status true
    '''
    # def get_object(self):
    #     return Post.objects.get(
    #         pk=self.kwargs["pk"],
    #         status=True
    #     )
    '''
    Add context of new name for feature of the post
    '''
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     context["name"] = "My Blog"

    #     return context

    '''
    This functoin for said the only user is login can see this post
    '''
    # def dispatch(self, request, *args, **kwargs):

    #     if not request.user.is_authenticated:
    #         return redirect("login")

    #     return super().dispatch(request, *args, **kwargs)

    '''
    This function you can filter the data
    '''
    def get_queryset(self):

        return Post.objects.filter(
            status=True
        )
    
class PostCreateView(CreateView):
    """
    This claad for create a new post with form
    """
    model = Post
    form_class = PostForm
    # success_url = '/blog/'

    '''
    Use the username of the user insted of user add it manual in the create form
    '''
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    '''
    Redirect user when create the post is successful
    '''
    def get_success_url(self):
        return reverse_lazy("blog:list_post")
    
class PostEditView(UpdateView):
    '''
    This class use for edit the post
    '''
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'
    pk_url_kwarg = "id"

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/post/'
    pk_url_kwarg = "id"