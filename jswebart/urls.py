"""
URL configuration for jswebart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from jswebart import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap, BlogPostSitemap


sitemaps = {
    'static': StaticSitemap,
    'blog': BlogPostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
    path("subscribe/", views.subscribe, name="subscribe"),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]



