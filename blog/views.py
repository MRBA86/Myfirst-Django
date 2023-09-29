from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone as tz
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def blog_view(request,**kwargs):
    posts =Post.objects.filter(published_date__lte= tz.now() , status = 1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)    
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request, pid):
    posts =Post.objects.filter(published_date__lte = tz.now() , status = 1)
    post = get_object_or_404(posts, pk=pid)
    post_next = Post.objects.filter(published_date__lte = tz.now() , status = 1, id__gt = pid).order_by('id').first()
    post_pre = Post.objects.filter(published_date__lte = tz.now() , status = 1, id__lt = pid).order_by('-id').first()
    context={'post':post,
             'post_next': post_next,
             'post_pre':post_pre}
    post.counted_views = post.counted_views + 1
    post.save()
    return render(request, 'blog/blog-single.html', context)

def blog_category(request,cat_name):
    posts =Post.objects.filter(published_date__lte= tz.now() , status = 1)
    posts = posts.filter(category__name = cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    posts =Post.objects.filter(published_date__lte= tz.now() , status = 1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)

    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

# Create your views here.
