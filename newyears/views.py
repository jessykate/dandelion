# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from newyears.models import *

# Create your views here.
@login_required
def index(request):
	nys = NewYear.objects.all()
	context = {'nys': nys}
	return render(request, 'newyears/index.html', context)

def detail(request, newyear_id):
	ny = get_object_or_404(NewYear, pk=newyear_id)
	context = {'ny': ny}
	return render(request, 'newyears/detail.html', context)

