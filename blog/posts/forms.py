from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserCreationForm
from posts.models import Post,Comment,Author
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class SignupForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    class Meta:
        model= User
        fields=['username','email','first_name','last_name','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    class Meta:
        model= User
        fields=['username','email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['profile_pic',]


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        widgets={
            'author':forms.TextInput(attrs={'class':'select form-control','value':'','id':'id_author','type':'hidden'}),
        }


class CommentForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Type Your Comment',
        'id':'usercomment',
        'rows':'4',
        }))
    class Meta:
        model=Comment
        fields=('content',)
