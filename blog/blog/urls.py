"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf import settings
from posts import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.index,name='home'),
    path('search/', v1.search,name='search'),
    path('blog/',v1.blog,name='post-list'),
    path('<int:pk>',v1.PostDetail.as_view()),
    path('pcreate/',v1.PostAdd.as_view()),
    path('update/<int:pk>',v1.PostUpdate.as_view()),
    path('delete/<int:pk>',v1.PostDelete.as_view()),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('sports/',v1.sports),
    path('business/',v1.business),
    path('food/',v1.food),
    path('travel/',v1.travel),
    path('gym/',v1.gym),
    path('gamming/',v1.gamming),


    path('draft/',v1.draft),
    path('authform/',v1.AuthorAdd),

    path('authorpost/',v1.view,name='post-list'),
    path('post/<id>/',v1.post,name='post-detail'),

    path('signup/',v1.Signup,name='signup'),

    path('logout/',v1.logout_view),
    path('accounts/',include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
