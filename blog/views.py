from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request, 'blog.html')

def blog_category(request, slug):
    return render(request, 'blog/blog_category.html')
