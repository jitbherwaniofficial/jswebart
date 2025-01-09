from django.urls import include, path

from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<slug:category_slug>/', views.blog_by_category, name='blog_by_category'),
    path('<slug:project_slug>/', views.content_page_view, name='blog_detail'),  # Project detail
]