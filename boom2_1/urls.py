
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from social_auth.views import complete
from django.conf import settings





admin.autodiscover()


urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT, }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),



    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^search_form/$', 'core.views.Search_form'),
    (r'^search/$', 'core.views.Search'),


    url(r'^associate/complete/(?P<backend>[^/]+)/$', 'customer.views.associate_complete_wrapper'),

    #url(r'^customers/login/$', 'core.views.login'),
    (r'^$','core.views.Index' ),
    #url(r'^(?P<slug>.*)/$', 'catalog'),
    #url(r'^catalog/(?P<slug>.*)/$' , 'catalog'),
    #url(r'^catalog/$' , 'catalog'),
    #url(r'^product/(?P<slug>[-/w]+)/$', 'product'),
    (r'^products/$', 'core.views.ProductsAll'),
    (r'^products/(?P<productslug>.*)/$', 'core.views.SpecificProduct'),
    (r'^products/(?P<productslug>.*)/$', 'core.views.ProductsAll'),
    (r'^vendors/(?P<vendorslug>.*)/$', 'core.views.SpecificVendor'),
    (r'^catalogues/$', 'core.views.CataloguesAll'),
    (r'^shops/$', 'core.views.Shops'),
    (r'^catalogues/(?P<catalogslug>.*)/$', 'core.views.SpecificCatalog'),
    (r'^shops/$', 'core.views.Shops'),
    (r'^profile/$','customer.views.profile'),
    (r'^addproduct/$','customer.views.addproduct'),
    (r'^dashboard/$','customer.views.dashboard'),

    #url(r'^social-auth/complete/$', csrf_exempt(complete), name='complete'),
    #url(r'^social-auth/', include('social_auth.urls')),






)














    
