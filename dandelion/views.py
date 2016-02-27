from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse 
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

def user_detail(request, user_id):
	user = get_object_or_404(User, id=user_id)
	return render(request, 'user.html', {'user': user})





