from django.urls import include, path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('branding-services/', views.branding_services, name='branding_services'),
    path('ui-ux-services/', views.ui_ux_services, name='ui_ux_services'),
    path('web-development-services/', views.web_development_services, name='web_development_services'),
    path('digital-marketing-services/', views.digital_marketing_services, name='digital_marketing_services'),
    path('packaging-design-services/', views.packaging_design_services, name='packaging_design_services'),
    path('print-design-services/', views.print_design_services, name='print_design_services'),
    path('contact/', views.contact, name='contact'),
    
]
