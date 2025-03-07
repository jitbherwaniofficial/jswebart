from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Portfolio, PortfolioCategory
from django.http import JsonResponse
from django.template.loader import render_to_string


def portfolio(request):
    portfolios = Portfolio.objects.all()
    categories = PortfolioCategory.objects.all()

      # By default, noindex for portfolio view (optional)
    noindex = False
    canonical_url = request.build_absolute_uri()

    # Check if it's an AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        content = render_to_string('partials/portfolio_items.html', {'portfolios': portfolios})
        return JsonResponse({'html': content})

    # For Portfolio view, you might want to add noindex or a canonical link
    noindex = True  # Optionally add noindex here if it's the main page

    return render(request, 'portfolio.html', {
        'categories': categories,
        'portfolios': portfolios,
        'current_category': None,
        'noindex': noindex,  
        'canonical_url': canonical_url, 
    })




def portfolio_by_category(request, category_slug):
    # Get category
    category = get_object_or_404(PortfolioCategory, slug=category_slug)
    # Filter portfolios by category
    portfolios = Portfolio.objects.filter(categories=category)

     # Add canonical URL or noindex logic here
    noindex = False
    canonical_url = request.build_absolute_uri()

    # Check if it's an AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Render only the portfolio items part of the page
        content = render_to_string('partials/portfolio_items.html', {
            'portfolios': portfolios,
            'current_category': category,
        })
        return JsonResponse({'html': content})

    return render(request, 'portfolio.html', {
        'categories': PortfolioCategory.objects.all(),
        'portfolios': portfolios,
        'current_category': category,
        'noindex': noindex,  # Flag for noindex if needed
        'canonical_url': canonical_url,  # The canonical link for the filtered page
    })



def portfolio_detail(request, project_slug):
    # Get the portfolio project
    portfolio = get_object_or_404(Portfolio, slug=project_slug)
    linked_categories = portfolio.categories.all()
    print(linked_categories)
    categories = PortfolioCategory.objects.all()
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio, 'categories':categories, 'linked_categories':linked_categories})


