from django.shortcuts import render


def front(request):
    return render(request, 'core/front.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')

def biography(request):
    return render(request, 'core/biography.html')