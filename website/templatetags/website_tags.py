from django import template
from django.utils import timezone as tz
from blog.models import Post

register = template.Library()

@register.filter
def snipets(value,args):
    return value[:args]

@register.inclusion_tag('website/website_latest_posts.html')
def website_latestposts(args=6):
    posts = Post.objects.filter(published_date__lte = tz.now(), status=1).order_by('published_date')[:args]
    return {'posts': posts}