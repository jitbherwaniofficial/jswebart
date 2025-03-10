from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),  # View all projects
    path('category/<slug:category_slug>/', views.portfolio_by_category, name='portfolio_by_category'),  # Filter by category
    path('<slug:project_slug>/', views.portfolio_detail, name='portfolio_detail'),  # Project detail
]



