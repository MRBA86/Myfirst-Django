from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post
from django.utils import timezone as tz


class LatestEntriesFeed(Feed):
    title = "Newest Post"
    link = "/rss/feed"
    description = "Updates on changes and additions to blog posts."

    def items(self):
        return Post.objects.filter(published_date__lte = tz.now() , status = 1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]

    # item_link is only needed if NewsItem has no get_absolute_url method.
    #def item_link(self, item):
    #    return reverse("news-item", args=[item.pk])