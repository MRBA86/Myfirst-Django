from django import template
from blog.models import Post
from django.utils import timezone as tz

register = template.Library()

@register.filter
def snipets(value,args):
    return value[:args] + "..."

@register.inclusion_tag('blog/blog-popular-posts.html')
def latesposts(args=3):
    posts = Post.objects.filter(published_date__lte = tz.now() , status = 1)[:args]
    return {'posts':posts}