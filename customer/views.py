from django.shortcuts import render
from django.http import HttpResponseRedirect
from customer.forms import Profile, Dashboard, Addproduct
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from social_auth.views import associate_complete

def associate_complete_wrapper(request, backend):
    try:
        return associate_complete(request, backend)
    except ValueError, e:
        if e and len(e.args) > 0:
            messages.error(request, "Failed to Associate: %s" % e.args[0])
    return redirect(reverse('dashboard'))


def profile(request):
    #if request.method == 'POST': # If the form has been submitted...
    form = Profile(request.POST or None) # A form bound to the POST data
    if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect('/index/') # Redirect after POST
    else:
    #    form = Profile() # An unbound form

            return render(request, 'profile.html', {
        'form': form,
        })



def dashboard(request):
        form = Dashboard(request.POST or None)

        if form.is_valid():
            dashboard = form.save(commit=False)
            dashboard.user = request.user
            dashboard.save()
            form.save()

            return HttpResponseRedirect('/addproduct/')
        else:
           return render(request, 'dashboard.html', {
        'form': form,
        })

def addproduct(request):
        form = Addproduct(request.POST or None) # A form bound to the POST data

        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/') # Redirect after POST
        else:
            return render(request, 'addproduct.html', {
            'form': form,
            })