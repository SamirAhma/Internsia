from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post

class StaticViewsSiteMap(Sitemap):
    changefreq = "monthly"
    def items(self):
        return ['joblist-home']
 
    def location(self, item):
        return reverse(item)

class PostViewsSiteMpa(Sitemap):
    def items(self):
        return Post.objects.all()