from django.contrib.sitemaps import Sitemap
from .models import Post
 
 
class PostSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated
        
    def location(self,obj):
        return f"/post/{obj.id}/{obj.slug}"
