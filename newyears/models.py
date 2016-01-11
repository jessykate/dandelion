from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NewYear(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	year = models.IntegerField()
	info = models.TextField(help_text="Location and other information about this event")
	start = models.DateTimeField()
	end = models.DateTimeField()
	# disable until Pillow install is sorted out.
	# picture = models.ImageField()

	def __str__(self):
		return '[%d] %s' % (self.year, self.name)

class Registration(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	event = models.ForeignKey(NewYear)
	arrive = models.DateTimeField()
	depart = models.DateTimeField()
	carpool = models.TextField()
	comments = models.TextField()
	room_preferences = models.TextField()
	status = models.CharField(max_length=200)
	user = models.ForeignKey(User)

class List(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200)
	newyear = models.ForeignKey(NewYear)

class ListComment(models.Model):
	text = models.TextField()
	user = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	the_list = models.ForeignKey(List)

