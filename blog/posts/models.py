from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Create your models here.


class Author(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    profile_pic=models.ImageField(upload_to='profile_pic', default='default.png')

    def __str__(self):
        return f'{self.user.username} Author'


class Category(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    post=models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class PostManager(models.Manager):
    def active(self,*args,**kwargs):
        return super(PostManager,self).get_queryset().filter(status='draft')



class  Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('publihsed','Publihsed'),
    )
    title=models.CharField(max_length=100)
    status=models.CharField(choices=STATUS_CHOICES,max_length=10,default=1)
    overview= models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    content=RichTextUploadingField(blank=True,null=True)
    author= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post_list', on_delete=models.CASCADE,default=False)
    thumbnail=models.ImageField()
    categories=models.ManyToManyField(Category)
    featured=models.BooleanField()
    previous_post=models.ForeignKey('self',related_name='previous', on_delete=models.SET_NULL,blank=True,null=True)
    next_post=models.ForeignKey('self',related_name='next',on_delete=models.SET_NULL,blank=True,null=True)
    objects=PostManager()


    def get_categories(self):
        return ",".join([str(p) for p in self.categories.all()])

    def __str__(self):
        return self.title

    def __str__(self):
        return self.status

    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={
                'id':self.id
        })
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')
    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()


class PostView(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey('Post',on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
