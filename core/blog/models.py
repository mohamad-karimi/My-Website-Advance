from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    '''
    This is make post for the blog app
    '''
    
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    published_date =models.DateField()


    def __str__(self):
        return self.title
    
class Category(models.Model):
    '''
    The Category for the post
    '''
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name