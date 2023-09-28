from django import template
from blog.models import Post
from blog.models import Category
from django.utils import timezone as tz

register = template.Library()

@register.filter
def snipets(value,args):
    return value[:args] + "..."

@register.inclusion_tag('blog/blog-popular-posts.html')
def latesposts(args=3):
    posts = Post.objects.filter(published_date__lte = tz.now() , status = 1)[:args]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(published_date__lte = tz.now() , status = 1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories :
        cat_dict[name] = posts.filter(category= name).count()
    return {'categories': cat_dict}

