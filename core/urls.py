from django.urls import include, path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('branding/', views.branding_services, name='branding_services'),
    path('ui-ux-design/', views.ui_ux_services, name='ui_ux_services'),
    path('web-development/', views.web_development_services, name='web_development_services'),
    path('digital-marketing/', views.digital_marketing_services, name='digital_marketing_services'),
    path('packaging-design/', views.packaging_design_services, name='packaging_design_services'),
    path('print-design/', views.print_design_services, name='print_design_services'),
    path('contact-us/', views.contact, name='contact'),
    path('thank-you/', views.thankyou, name='thankyou'),
    path('success/', views.success, name='success'),
    path('join-us/', views.joinus, name='join_us'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditons, name='terms_and_conditions'),
    
]
