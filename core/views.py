from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from blog.forms import SubscriptionForm
from blog.models import Blog
from .forms import ContactForm, JoinUsForm
from decouple import config

# Create your views here. 



def home(request): 
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
    SITE_KEY = config('SITE_KEY')
    if request.method == 'POST':
        print("POST data received:", request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid. Saving data.")
            form.save()
            request.session['form_submitted'] = True # Session flag
            return redirect('thankyou')
        else:
            print("Form errors:", form.errors)
            return render(request, 'contact-us.html', {'form': form, 'errors': form.errors})
    else:
        form = ContactForm()
    return render(request, 'contact-us.html', {'form': form, 'SITE_KEY':SITE_KEY})


def thankyou(request):
    # WE HAVE TO CHECK IF SESSION FLAG EXISTS OR NOT
    if request.session.get('form_submitted', False):
        # WE HAVE TO DELETE THE FLAG TO PREVENT DIRECT ACCESS ON REFRESH
        del request.session['form_submitted'] # THIS WILL REMOVE THE FLAG
        return redirect('thankyou')
    else:
        return render(request, 'contact-us.html') # IF AN HACKER IS HARDCODING 'THANK-YOU' ON URL THEN REDIRECT THAT STUPID FELLOW TO CONTACT PAGE



def joinus(request):
    SITE_KEY = config('SITE_KEY')
    if request.method == 'POST':
        form = JoinUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the model
            request.session['joinus_form_submitted'] = True # Session flag
            return redirect('success')  # Redirect to the success page after form submission
        else:
            return render(request, 'joinus.html', {'form': form, 'success': False})
    else:
        form = JoinUsForm()
    return render(request, 'joinus.html', {'form': form, 'SITE_KEY':SITE_KEY})


def success(request):
    # WE HAVE TO CHECK IF SESSION FLAG EXISTS OR NOT
    if request.session.get('joinus_form_submitted', False):
        # WE HAVE TO DELETE THE FLAG TO PREVENT DIRECT ACCESS ON REFRESH
        del request.session['joinus_form_submitted'] # THIS WILL REMOVE THE FLAG
        return redirect('success')
    else:
        return render(request, 'joinus.html') # IF AN HACKER IS HARDCODING 'THANK-YOU' ON URL THEN REDIRECT THAT STUPID FELLOW TO JOIN US PAGE

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def terms_and_conditons(request): 
    return render(request, 'terms-and-conditions.html')


