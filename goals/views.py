from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse 
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Q

from goals.models import *
from goals.forms import *

@login_required
def goal_list(request, year):
    goals_list = Goals.objects.filter(year__year=year).filter(Q(user=request.user) | Q (shared_with=request.user))
    print goals_list
    context = {'goals_list': goals_list, 'year': year}
    return render(request, 'goals/index.html', context)

def create(request):
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = GoalsForm(request.POST) # check whether it's valid: 
		if form.is_valid():
			g = form.save(commit=False)
			g.user = request.user
			g.save()
			return HttpResponseRedirect(reverse('goals:detail', args=(g.id,)))
    # if a GET (or any other method) we'll create a blank form
	else:
		form = GoalsForm()
	context = {'form': form}
	return render(request, 'goals/create.html', context)

def detail(request, goals_id):
    goals = Goals.objects.get(id=goals_id)
    print goals.user
    print request.user
    if goals.user != request.user and request.user not in goals.shared_with.all():
        messages.add_message(request, messages.INFO, 'You are not authorized to view that page.')
        return HttpResponseRedirect("/404")
    context = {'goals': goals}
    return render(request, 'goals/detail.html', context)
