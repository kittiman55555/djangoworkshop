from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.


def index(request):
    listing = Listing.objects.order_by('list_date').filter(is_published=True)[:3]
    context = {
        'listings' : listing
    }
    return render(request, 'pages/index.html', context)

def about(request):
       #get all relator
    relators  = Realtor.objects.order_by('hire_date')
    
    #get all
    mvp_relators = Realtor.objects.all().filter(is_mvp=True)
    context ={
        'relators' : relators,
        'mvp_relators' : mvp_relators

    }
    return render(request, 'pages/about.html', context)

def listing(request):
 
    return render(request, 'listings/listings.html')