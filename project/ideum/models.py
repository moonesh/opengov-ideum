from django.db import models
from django.db.models import permalink
from datetime import datetime
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic, e.g. 'street'"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(
            max_length=255,
            help_text="Automatically built from the name.",)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Citizen(User):
    """The main actor based on the default User class."""
    name = models.CharField(max_length=256, blank=False, null=False)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('username',)

    def get_absolute_url(self):
        return "/user/%s/" % self.id


class Pingback(models.Model):
    """A pingback for a specific idea,"""
    title = models.CharField(max_length=512)
    url = models.URLField(verify_exists=False)
    text = models.TextField(blank=True)
    idea = models.ForeignKey('Idea', related_name='pingbacks')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)



class Vote(models.Model):
    """A vote for an idea"""
    voter = models.ForeignKey(Citizen, related_name='votes')
    idea = models.ForeignKey('Idea', related_name='votes')
    created_date = models.DateTimeField(default=datetime.now)


class Idea(models.Model):
    """An idea submitted by a citizen."""
    title = models.CharField(max_length=512)
    text = models.TextField(blank=False)
    enable_comments = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now)
    start_date = models.DateTimeField(blank=True, null=True)
    closing_date = models.DateTimeField(blank=True, null=True)
    topics = models.ManyToManyField(Topic, related_name='ideas', blank=True)	
    submitter = models.ForeignKey(Citizen, related_name='ideas')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/idea/%s/" % self.id


