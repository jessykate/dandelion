from django.contrib import admin

# Register your models here.
from newyears.models import *

class NewYearAdmin(admin.ModelAdmin):
	model = NewYear

class RegistrationAdmin(admin.ModelAdmin):
	model = NewYear

class ListCommentInline(admin.TabularInline):
	model = ListComment

class ListAdmin(admin.ModelAdmin):
	model = NewYear
	inlines = [ListCommentInline,]

admin.site.register(NewYear, NewYearAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(List, ListAdmin)



