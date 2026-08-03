from django.contrib import admin
from blog.models import Post, Category

# Register your models here.
class CustomPostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ("title", "author", "status", "category", "published_date")
    list_filter = ("status", "author")
    readonly_fields = ("create_date", "update_date")
    fieldsets = (
        ("New Post", {"fields": ("title", "author", "image", "content", "status", "category", "published_date")}),
    )

    add_fieldsets = (
        ("New Post", {"fields": ("title", "author", "image", "content", "status", "category", "published_date")}),
    )

    search_fields = ("title", "content")
    ordering = ("published_date",)

admin.site.register(Post, CustomPostAdmin)
admin.site.register(Category)