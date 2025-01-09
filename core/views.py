from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from blog.forms import SubscriptionForm
from blog.models import Blog
from .forms import ContactForm, JoinUsForm

# Create your views here. 

def home(request):
    form = SubscriptionForm()
    if request.method == "POST":
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check for AJAX request
            form = SubscriptionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Thank you for subscribing!")
                return JsonResponse({"success": True, "message": "Thank you for subscribing!"})
            else:
                return JsonResponse({"success": False, "message": "Failed to subscribe. This Email is already in use."})
    all_post = Blog.objects.order_by('-created_at')[:3]
    return render(request, 'home.html', {'all_post': all_post}) 


def about_us(request):
    return render(request, 'about-us.html')

def branding_services(request):
    return render(request, 'branding_services.html')

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
    if request.method == 'POST':
        print("POST data received:", request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid. Saving data.")
            form.save()
            return redirect('thankyou')
        else:
            print("Form errors:", form.errors)
            return render(request, 'contact-us.html', {'form': form, 'errors': form.errors})
    else:
        form = ContactForm()
    return render(request, 'contact-us.html', {'form': form})


def thankyou(request):
    return render(request, 'thankyou.html')



def joinus(request):
    if request.method == 'POST':
        form = JoinUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the model
            return redirect('success')  # Redirect to the success page after form submission
        else:
            return render(request, 'joinus.html', {'form': form, 'success': False})
    else:
        form = JoinUsForm()
    return render(request, 'joinus.html', {'form': form})


def success(request):
    return render(request, 'success.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def terms_and_conditons(request): 
    return render(request, 'terms-and-conditions.html')
