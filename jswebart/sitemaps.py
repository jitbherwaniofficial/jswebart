# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from datetime import datetime
from blog.models import Blog

# Priority groups
PRIORITY_GROUPS = {
    'tier1': ['home', 'branding_services', 'ui_ux_services', 'web_development_services',
              'digital_marketing_services', 'packaging_design_services', 'print_design_services'],
    'tier2': ['about_us', 'blog', 'contact', 'join_us'],
    'tier3': ['privacy_policy', 'terms_and_conditions']
}

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    
    def items(self):
        # Combine all URL names
        return [
            *PRIORITY_GROUPS['tier1'],
            *PRIORITY_GROUPS['tier2'],
            *PRIORITY_GROUPS['tier3']
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item in PRIORITY_GROUPS['tier1']:
            return 1.0  # Highest priority
        elif item in PRIORITY_GROUPS['tier2']:
            return 0.6  # Medium priority
        return 0.3  # Lowest priority

    def lastmod(self, item):
        # Static pages use fixed date (update as needed)
        return datetime(2025, 3, 10)

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0  # Blog posts in Tier 1

    def items(self):
        return Blog.objects.filter(is_published=True)

    def location(self, item):
        return reverse('blog_detail', kwargs={'project_slug': item.slug})

    def lastmod(self, item):
        return item.updated_at