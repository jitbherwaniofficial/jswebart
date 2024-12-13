from django.urls import include, path

from portfolio import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<slug:slug>/', views.portfolio_detail,name='portfolio_detail'),
]