from django.contrib import admin

# Register your models here.
from goals.models import *

class GoalsAdmin(admin.ModelAdmin):
	model = Goals

admin.site.register(Goals, GoalsAdmin)

