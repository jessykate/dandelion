from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse 
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from goals.models import Goals
from newyears.models import NewYear

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user == user:
        goals = {}
        for year in NewYear.objects.years():
            goals_this_year = user.goals_set.filter(year=year)
            goals[year] = goals_this_year
    else:
        #goals = user.goals_set.filter(shared_with=request.user)
        goals = {}
        for year in NewYear.objects.years():
            visible_year_goals = Goals.objects.pairwise_visible(year, request.user, user)
            goals[year] = visible_year_goals

    return render(request, 'user.html', {'user': user, 'goals': goals})





