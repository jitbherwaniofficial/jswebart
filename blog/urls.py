from django.urls import include, path

from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog/<slug:category>/', views.blog_category, name='blog_category'),
]