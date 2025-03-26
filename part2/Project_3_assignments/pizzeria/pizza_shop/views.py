from django.shortcuts import render


def index(request):
    """The home page for the Pizza shop"""
    return render(request, 'pizza_shop/index.html')


