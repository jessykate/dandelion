from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse 
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user == user:
        goals = user.goals_set.all().order_by('year')
    else:
        goals = user.goals_set.filter(shared_with=request.user)

    return render(request, 'user.html', {'user': user, 'goals': goals})





