from django.forms import ModelForm
from django import forms
from goals.models import *

class ListForm(ModelForm):
	class Meta:
		model = List
		exclude = ['user', 'newyear']

class ListCommentForm(ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control"}))
	class Meta:
		model = ListComment
		exclude = ['user', 'the_list']


