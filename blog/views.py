from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone as tz


def blog_view(request):
    posts =Post.objects.filter(published_date__lte= tz.now() , status = 1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request, pid):
    posts =Post.objects.filter(published_date__lte = tz.now() , status = 1)
    post = get_object_or_404(posts, pk=pid)
    context={'post':post}
    post.counted_views = post.counted_views + 1
    post.save()

    return render(request, 'blog/blog-single.html', context)

# Create your views here.
