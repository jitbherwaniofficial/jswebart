from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about-us.html')

def branding_services(request):
    return render(request, 'branding-services.html')

def ui_ux_services(request):
    return render(request, 'ui-ux-services.html')

def web_development_services(request):
    return render(request, 'web-development-services.html')

def digital_marketing_services(request):
    return render(request, 'digital-marketing-services.html')

def packaging_design_services(request):
    return render(request, 'packaging-design-services.html')

def print_design_services(request):
    return render(request, 'print-design-services.html')

def contact(request):
    return render(request, 'contact.html')
