from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone as tz


def blog_view(request):
    posts =Post.objects.exclude(published_date__gte = tz.now())
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request, pid):
    posts =Post.objects.exclude(published_date__gte = tz.now())
    post = get_object_or_404(posts, pk=pid)
    post.counted_views = post.counted_views + 1
    post.save()
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)


def test(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/test.html', context)
# Create your views here.
