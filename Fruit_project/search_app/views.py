from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from shop.models import Product
from django.db.models import Q

from django.views.generic import ListView
from django.db.models import Q


def search_results(request):
    products=None
    query=None
    if 'q' in request.POST:
        query = request.POST.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request, 'search.html', {'query': query, 'products': products})



