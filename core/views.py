# Create your views here.
from core.models import Product, Catalog, Category, Vendor
from django.http import HttpResponse
from django.template import Context, loader
#from annoying.decorators import render_to
from django.shortcuts import render_to_response
from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponse, Http404

from django.views.generic.simple import direct_to_template
def Index(request):
    products = Product.objects.all().order_by('name')
    context = {'products': products}
    return render_to_response('index.html', context, context_instance = RequestContext(request))


def ProductsAll(request):
    products = Product.objects.all().order_by('name')
    context = {'products': products}
    return render_to_response('productsall.html', context, context_instance = RequestContext(request))


def SpecificProduct(request, productslug):
    product = Product.objects.get(slug = productslug)
    context = {'product': product}
    return render_to_response('specificproduct.html', context, context_instance = RequestContext(request))

def SpecificVendor(request, vendorslug):
    vendor = Vendor.objects.get(slug=vendorslug)
    products = Product.objects.filter(vendor=vendor)
    context = {'vendor': vendor, 'products': products}
    return render_to_response('specificvendor.html', context, context_instance=RequestContext(request))

def CataloguesAll(request):
    catalogues = Catalog.objects.all().order_by('name')
    context = {'catalogues': catalogues}
    return render_to_response('catalogues.html', context, context_instance = RequestContext(request))


def SpecificCatalog(request, catalogslug):
    catalog = Catalog.objects.get(slug = catalogslug)
    products = Product.objects.filter(catalog = catalog)
    context = {'products': products}
    return render_to_response('specificcatalog.html', context, context_instance=RequestContext(request))

def Shops(request):
    vendor = Vendor.objects.all()
    context = {'vendor': vendor}
    return render_to_response('shops.html',context, context_instance=RequestContext(request))


def Search_form(request):
    return render(request, 'search_form.html')

def Search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            products = Product.objects.filter(name__icontains=q)
            return render(request, 'search_results.html',
                    {'products': products, 'query': q})
    return render(request, 'search_form.html',
            {'error': error})