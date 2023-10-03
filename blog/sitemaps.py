from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.utils import timezone as tz
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(published_date__lte= tz.now(), status = 1)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, item):
        return reverse('blog:single',kwargs={'pid':item.id})
    