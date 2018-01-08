# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse 
from django.core.urlresolvers import reverse

from newyears.models import *
from newyears.forms import *

# Create your views here.
@login_required
def index(request):
	nys = NewYear.objects.all().order_by('-year')
	context = {'nys': nys}
	return render(request, 'newyears/index.html', context)

def newyear_detail(request, newyear_id):
	ny = get_object_or_404(NewYear, pk=newyear_id)
	context = {'ny': ny}
	return render(request, 'newyears/newyear_detail.html', context)

def list_create(request, newyear_id):
	ny = get_object_or_404(NewYear, pk=newyear_id)
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = ListForm(request.POST) # check whether it's valid: 
		if form.is_valid():
			lst = form.save(commit=False)
			lst.user = request.user
			lst.newyear = ny
			lst.save()
			return HttpResponseRedirect(reverse('newyears:list_detail', args=(ny.id, lst.id,)))
    # if a GET (or any other method) we'll create a blank form
	else:
		form = ListForm()
	context = {'form': form, 'ny': ny}
	return render(request, 'newyears/list_create.html', context)



def list_detail(request, newyear_id, list_id):
	lst = get_object_or_404(List, pk=list_id)
	if request.method == 'POST':
		form = ListCommentForm(request.POST) # check whether it's valid: 
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = request.user
			comment.the_list = lst
			comment.save()
			return HttpResponseRedirect(reverse('newyears:list_detail', args=(newyear_id, lst.id,)))
    # if a GET (or any other method) we'll create a blank form
	else:
		form = ListCommentForm()
	context = {'form': form, 'l': lst, 'newyear_id': newyear_id}
	return render(request, 'newyears/list_detail.html', context)


