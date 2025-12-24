from django.shortcuts import render

# Create your views here.
def listings(request):
    print(f'request: {request}, request.path: {request.path}')
    return render(request, 'listings/listings.html')

def listing(request, listing_id):
    print(f'request: {request}, request.path: {request.path}')
    return render(request, 'listings/listing.html')

def search(request):
    print(f'request: {request}, request.path: {request.path}')
    return render(request, 'listings/search.html')