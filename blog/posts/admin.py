from django.contrib import admin
from posts.models import Category,Post,Comment,PostView,Author
from posts.forms import PostForm,ProfileUpdateForm
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=['user','profile_pic']
admin.site.register(Author,AuthorAdmin)
admin.site.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','status','overview','timestamp','author','thumbnail','get_categories','featured']
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(PostView)
