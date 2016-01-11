from django.forms import ModelForm
from goals.models import *

class GoalsForm(ModelForm):
	class Meta:
		model = Goals
		exclude = ['user',]

