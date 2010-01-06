# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.cache import cache_page
from ideum.models import *
from ideum.forms import *
#from util.comments_extra import post_comment
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.comments.views.comments import CommentPostBadRequest 
from django.contrib.comments.views.utils import next_redirect
from django.contrib import comments
from django.contrib.comments.models import Comment
from django.contrib.comments import signals
from django.utils.translation import ugettext as _
from django.db.models import Count


# Start page
def index(request):
    # Get list of ideas
    ideas = Idea.objects.annotate(Count('votes')).order_by("-votes__count")[:20]

    if request.method == 'POST': # If the form has been submitted...
        form = IdeaForm(request.POST) # A form bound to the POST data
        if form.is_valid():

            # find or create submitter based on email address
            submitter = None
            try:
                submitter = Citizen.objects.get(email__exact=form.cleaned_data['submitter_email'])
            except Citizen.DoesNotExist:
                submitter = Citizen()
                submitter.name = form.cleaned_data['submitter_name']
                submitter.email = form.cleaned_data['submitter_email']
                submitter.save()

            i =Idea()
            i.title = form.cleaned_data['title']
            i.text = form.cleaned_data['text']
            i.submitter = submitter
            i.save()

            return HttpResponseRedirect('/page/thankyou/') # Redirect to thenak you page after POST
        else:
            pass

    form = IdeaForm()

    page_title = _("Welcome!")
    return render_to_response('index.html', locals())


# Single idea
def idea(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)    
    submitter_idea_count = None
    if idea.submitter.ideas.all():
        submitter_idea_count = len(idea.submitter.ideas.all())
    page_title = idea.title
    return render_to_response('idea.html', locals())

# Atom feed with params for topics

# Login

# Create account

# Thank you for creating account

# Account edit (wih idea list)

# Create new idea

# Thank you
def thankyou(request):
    """Page shown after submitting an idea."""
    page_title = _("Thank you for sharing your idea!")
    return render_to_response('thankyou.html', locals())

# Handle pingback

# Register vote

# Save comment


