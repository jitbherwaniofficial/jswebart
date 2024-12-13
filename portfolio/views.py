from django.shortcuts import render

# Create your views here.

def portfolio(request):
    return render(request, 'portfolio.html')

def portfolio_detail(request,slug):
    return render(request, 'portfolio_detail.html')