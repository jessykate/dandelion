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
    goals_list = Goals.objects.visible_for_user(year, request.user)
    context = {'goals_list': goals_list, 'year': year}
    return render(request, 'goals/index.html', context)

def create(request):
    if request.method == 'POST':
        form = GoalsForm(request.POST) # check whether it's valid: 
        if form.is_valid():
            g = form.save(commit=False)
            g.user = request.user
            if Goals.objects.filter(user=request.user, year=g.year).count() == 0:
                # if this is the first goals doc from this year, make it primary
                g.primary = True
            # the object must have a primary key before adding m2m field values
            g.save()
            form.save_m2m()
            #if request.POST.get('individual_sharing'):
            #    g.individual_sharing = request.POST.get('individual_sharing', None)
            #    g.save()
            #if request.POST.get('group_sharing'):
            #    g.group_sharing = request.POST.get('group_sharing', None)
            #    g.save()
            return HttpResponseRedirect(reverse('goals:detail', args=(g.id,)))
    else:
        form = GoalsForm()
        print form.fields
    context = {'form': form}
    return render(request, 'goals/create.html', context)

def detail(request, goals_id):
    goals = Goals.objects.get(id=goals_id)
    print goals.user
    print request.user
    if not goals.visible_to(request.user):
        messages.add_message(request, messages.INFO, 'You are not authorized to view that page.')
        return HttpResponseRedirect("/404")
    context = {'goals': goals}
    return render(request, 'goals/detail.html', context)
