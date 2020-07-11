from django.shortcuts import render,get_object_or_404,redirect,reverse
from .forms import  PostForm,CommentForm,SignupForm, UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment,PostView,Author
from django.db.models import Count, Q
from django.views import generic
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib import messages


@login_required
def gamming(request):
    sports=Post.objects.filter(categories__title = "Gamming Blog")
    auther=Author.objects.filter(user=request.user)
    post_list= Post.objects.all()
    category_count=get_category_count()
    most_recent=Post.objects.order_by('-timestamp')[:4]
    paginator=Paginator(post_list,4)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except  EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)
    context={'sports':sports,'auther':auther,'post_list':post_list,
        'querysets':paginated_queryset,
        'most_recent':most_recent,
        'category_count':category_count,
        'page_request_var':page_request_var,
        }
    return render(request, "game.html", context)
#------------------------------
@login_required
def gym(request):
    sports=Post.objects.filter(categories__title__icontains = "Gym And Health Blog")
    auther=Author.objects.filter(user=request.user)
    post_list= Post.objects.all()
    category_count=get_category_count()
    most_recent=Post.objects.order_by('-timestamp')[:4]
    paginator=Paginator(post_list,4)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except  EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)
    context={'sports':sports,'auther':auther,'post_list':post_list,
        'querysets':paginated_queryset,
        'most_recent':most_recent,
        'category_count':category_count,
        'page_request_var':page_request_var,
        }
    return render(request, "gym.html", context)


#------------------------------
@login_required
def business(request):
    sports=Post.objects.filter(categories__title__icontains = "business Blog")
    auther=Author.objects.filter(user=request.user)
    post_list= Post.objects.all()
    category_count=get_category_count()
    most_recent=Post.objects.order_by('-timestamp')[:4]
    paginator=Paginator(post_list,4)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except  EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)
    context={'sports':sports,'auther':auther,'post_list':post_list,
        'querysets':paginated_queryset,
        'most_recent':most_recent,
        'category_count':category_count,
        'page_request_var':page_request_var,
        }
    return render(request, "business.html", context)


#------------------------------
@login_required
def food(request):
    sports=Post.objects.filter(categories__title = "Foodiee Blogs")
    auther=Author.objects.filter(user=request.user)
    post_list= Post.objects.all()
    category_count=get_category_count()
    most_recent=Post.objects.order_by('-timestamp')[:4]
    paginator=Paginator(post_list,4)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except  EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)
    context={'sports':sports,'auther':auther,'post_list':post_list,
        'querysets':paginated_queryset,
        'most_recent':most_recent,
        'category_count':category_count,
        'page_request_var':page_request_var,
        }
    return render(request, "food.html", context)


#------------------------------
@login_required
def travel(request):
    sports=Post.objects.filter(categories__title__icontains = "Travel Blog")
    auther=Author.objects.filter(user=request.user)
    post_list= Post.objects.all()
    category_count=get_category_count()
    most_recent=Post.objects.order_by('-timestamp')[:4]
    paginator=Paginator(post_list,4)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except  EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)
    context={'sports':sports,'auther':auther,'post_list':post_list,
        'querysets':paginated_queryset,
        'most_recent':most_recent,
        'category_count':category_count,
        'page_request_var':page_request_var,
        }
    return render(request, "travel.html", context)


#------------------------------
@login_required
def sports(request):
    sports=Post.objects.filter(categories__title__icontains = "Sports Blog")
    auther=Author.objects.filter(user=request.user)
    post_list= Post.objects.all()
    category_count=get_category_count()
    most_recent=Post.objects.order_by('-timestamp')[:4]
    paginator=Paginator(post_list,4)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except  EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)
    context={'sports':sports,'auther':auther,'post_list':post_list,
        'querysets':paginated_queryset,
        'most_recent':most_recent,
        'category_count':category_count,
        'page_request_var':page_request_var,
        }
    return render(request, "sports.html", context)



@login_required
def draft(request):
    auth=Post.objects.filter(author = request.user).order_by('-timestamp').filter(status__icontains='draft')
    auther=Author.objects.filter(user=request.user)
    post_list= Post.objects.all()
    category_count=get_category_count()
    most_recent=Post.objects.order_by('-timestamp')[:4]
    paginator=Paginator(post_list,4)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except  EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)
    context={'auth':auth,'auther':auther,'post_list':post_list,
        'querysets':paginated_queryset,
        'most_recent':most_recent,
        'category_count':category_count,
        'page_request_var':page_request_var,
        }
    return render(request, "draft.html", context)


@login_required
def view(request):

    auth=Post.objects.filter(author = request.user).order_by('-timestamp').filter(status__icontains='Publihsed')
    auther=Author.objects.filter(user=request.user)
    post_list= Post.objects.all()
    category_count=get_category_count()
    most_recent=Post.objects.order_by('-timestamp')[:4]
    paginator=Paginator(post_list,4)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except  EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)
    context={'auth':auth,'auther':auther,
        'querysets':paginated_queryset,
        'most_recent':most_recent,
        'category_count':category_count,
        'page_request_var':page_request_var,
        }
    return render(request, "authorpost_list.html", context)


def search(request):
    queryset=Post.objects.all()
    query=request.GET.get('q')
    if query:
        queryset=queryset.filter(Q(title__icontains=query)|Q(overview__icontains=query)|Q(status__icontains=query)|Q(categories__title__icontains=query)).distinct()
    context={'queryset':queryset}
    return render(request,'search_result.html',context)


def get_category_count():
    queryset=Post\
            .objects\
            .values('categories__title')\
            .annotate(Count('categories__title'))
    return queryset

def index(request):
    category_count=get_category_count()
    featured=Post.objects.filter(featured=True)[0:3]
    latest=Post.objects.order_by('-timestamp')[0:6]
    context={'object_list':featured,'latest':latest,'category_count':category_count,}
    return render(request,'index.html',context)

@login_required
def blog(request):
    category_count=get_category_count()
    most_recent=Post.objects.order_by('-timestamp')[:5]
    auth=Author.objects.filter(user=request.user)
    post_list= Post.objects.all().order_by('-timestamp').filter(status__icontains='Publihsed')
    paginator=Paginator(post_list,6)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except  EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)
    context={'auth':auth,
        'queryset':paginated_queryset,
        'most_recent':most_recent,
        'category_count':category_count,
        'page_request_var':page_request_var,
        }
    return render(request,'posts/post_list.html',context)

def autherblog(request):
    auth=Author.objects.filter(author = request.user)
    return render(request,'base.html',{'auth':auth})



@method_decorator(login_required, name='dispatch')
class PostDetail(DetailView):
    model=Post
class PostAdd(CreateView):
    model=Post
    fields=('title','status','overview','content','author','thumbnail','categories','featured')
class PostUpdate(UpdateView):
    model=Post
    fields=('title','status','overview','content','author','thumbnail','categories','featured')
class PostDelete(DeleteView):
    model=Post
    success_url=reverse_lazy('home')


def post(request,id):
    category_count=get_category_count()
    auth=Author.objects.filter(user=request.user)
    most_recent=Post.objects.order_by('-timestamp')[:4]
    post=get_object_or_404(Post,id=id)
    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user,post=post)
    form=CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user=request.user
            form.instance.post=post
            form.save()
            return redirect(reverse('post-detail',kwargs={
                    'id':post.pk
            }))
    context={'post':post,'auth':auth,
        'form':form,
        'most_recent':most_recent,
        'category_count':category_count,
        }
    return render(request,'post.html',context)


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created For {username}!')
            return HttpResponseRedirect('/accounts/login')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})

def AuthorAdd(request):
    if request.method=='POST':
        u_form= UserUpdateForm(request.POST,instance=request.user)
        p_form= ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.author)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.author)

    context={
        'u_form':u_form,
        'p_form':p_form,
        }
    return render(request,'posts/author_form.html',context)


def logout_view(request):
    return render(request,'logout.html')
