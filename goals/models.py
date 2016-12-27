from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from newyears.models import *

# Create your models here.
class Goals(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    year = models.ForeignKey(NewYear)
    text = models.TextField()
    shared_with = models.ManyToManyField(User, related_name="shared_with")

    class Meta:
        verbose_name_plural = 'Goals'

    def __str__(self):
        return '%d Goals from %d/%d/%d' % (self.year.year, self.created.month, self.created.day, self.created.year)



