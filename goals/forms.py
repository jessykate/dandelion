from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from goals.models import *
from newyears.models import *
from django import forms

def year_choices():
    years = NewYear.objects.years()
    return [(year, '%s' % str(year)) for year in years]

class GoalsForm(ModelForm):
    year = forms.ChoiceField(choices=year_choices)
    class Meta:
        model = Goals
        exclude = ['user', 'primary']
        #field_classes = ['form-control',]
        labels = { 
            'individual_sharing': _('Additional individuals to share with'), 
            'group_sharing': _('Attendees to share with'), 
        }
        help_texts = { 
            'individual_sharing': _('Add any other specific individuals you wish to share with.'), 
            'group_sharing': _('Which groups of attendees would you like to share your goals with?'), 
        } 
        #error_messages = { 'name': { 'max_length': _("This writer's name is too long."), }, }



