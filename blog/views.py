from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
from django.shortcuts import render, get_object_or_404

from blog.forms import SubscriptionForm
from .models import Blog, BlogCategory, ContentSection


# View for all blog posts
def blog(request):
    posts = Blog.objects.all().order_by('-created_at')
    categories = BlogCategory.objects.all()

      # By default, noindex for portfolio view (optional)
    noindex = False
    canonical_url = request.build_absolute_uri()

    # Check if it's an AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        content = render_to_string('partials/blog_items.html', {'posts': posts, 'categories': categories,'current_category': None})
        return JsonResponse({'html': content})

        # For Blog view, you might want to add noindex or a canonical link
    noindex = True  # Optionally add noindex here if it's the main page
    return render(request, 'blog.html', {
        'posts': posts, 
        'categories': categories, 
        'current_category': None, 
        'noindex': noindex,  
        'canonical_url': canonical_url, 
    })

# View for filtered posts by category
def blog_by_category(request, category_slug):
    category = get_object_or_404(BlogCategory, slug=category_slug)
    posts = Blog.objects.filter(categories=category).order_by('-created_at')
    categories = BlogCategory.objects.all()

     # Add canonical URL or noindex logic here
    noindex = False
    canonical_url = request.build_absolute_uri()


     # Check if it's an AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Render only the portfolio items part of the page
        content = render_to_string('partials/blog_items.html', {
            'posts': posts,
            'current_category': category,
            'categories':categories
        })
        return JsonResponse({'html': content})

    return render(request, 'blog.html', {
        'posts': posts, 
        'categories': categories, 
        'current_category': category,
        'noindex': noindex,  # Flag for noindex if needed
        'canonical_url': canonical_url,  # The canonical link for the filtered page
    })


def blog_detail(request, project_slug):
    # Get the portfolio project
    post = get_object_or_404(Blog, slug=project_slug)
    all_post = Blog.objects.exclude(id=post.id).order_by('-created_at')[:2]
    linked_categories = post.categories.all()  # Categories linked to the blog
    categories = BlogCategory.objects.all()
    context = {
        'linked_categories': linked_categories,
        'post': post,
        'categories':categories,
        'all_post': all_post
    }
    return render(request, 'blog_detail.html', context)



def content_page_view(request, project_slug):
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
    
    page = get_object_or_404(Blog, slug=project_slug)
    sections = page.sections.all()
    all_post = Blog.objects.exclude(id=page.id).order_by('-created_at')[:2]
    categories = BlogCategory.objects.all()
    
    return render(request, 'blog_detail.html', {'page': page, 'sections': sections,'all_post': all_post,'categories':categories,'form': form})




