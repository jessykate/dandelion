from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from newyears.models import *

class GoalsManager(models.Manager):

    def visible_for_user(self, year, user):
        year_goals = Goals.objects.filter(year=year)

        user_goals = year_goals.filter(user=user) 
        individually_shared = year_goals.filter(individual_sharing=user)
        group_shared = year_goals.filter(group_sharing__attendees=user)
        
        goals_list = list(user_goals) + list(individually_shared) + list(group_shared)
        return goals_list

    def pairwise_visible(self, year, viewer, owner):
        # goals created by owner
        year_goals = Goals.objects.filter(year=year).filter(user=owner)
        visible = []
        for goal in year_goals:
            if goal.visible_to(viewer):
                visible.append(goal)
        return visible

# Create your models here.
class Goals(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    year = models.IntegerField()
    text = models.TextField()
    group_sharing = models.ManyToManyField(NewYear, related_name="group_sharing", blank=True)
    individual_sharing = models.ManyToManyField(User, related_name="individual_sharing", blank=True)
    primary = models.BooleanField(default=False)
    objects = GoalsManager()

    class Meta:
        verbose_name_plural = 'Goals'

    def __str__(self):
        return '%d Goals from %d/%d/%d' % (self.year, self.created.month, self.created.day, self.created.year)

    def visible_to(self, requesting_user):
        if requesting_user == self.user:
            return True
        if requesting_user in self.individual_sharing.all():
            return True
        for event in self.group_sharing.all():
            if requesting_user in event.attendees.all():
                return True
        return False

    def shared_with(self):
        people = list(self.individual_sharing.all())
        for event in self.group_sharing.all():
            for attendee in list(event.attendees.all()):
                people.append(attendee)
        return list(set(people))






