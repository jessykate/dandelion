from django.conf import settings # import the settings file
from newyears.models import NewYear

def goal_years(request):
    years = NewYear.objects.order_by('year').distinct('year').only('year')
    return {'GOAL_YEARS': years}
