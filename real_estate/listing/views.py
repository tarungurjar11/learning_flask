from django.shortcuts import render
from .models import Listing
# Create your views here.


def real_estate_list(request):
    listings = Listing.objects.all()
    context = {
        "listings" : listings
    }
    return render( request, "listings.html", context)