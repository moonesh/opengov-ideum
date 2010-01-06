# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django import forms
from django.forms import ModelForm
from models import Idea
from django.utils.safestring import mark_safe

class IdeaForm(forms.Form):
    """Form used to submit a new idea on the site."""

    # Idea title
    title = forms.CharField(label=_("I suggest that"), required=True, max_length=512)

    # Idea description
    text = forms.CharField(label=_("Describe your idea (be as specific as possible)"), required=True,widget=forms.widgets.Textarea(attrs={'rows':4, 'cols':40}))

    # Name of submitter
    submitter_name = forms.CharField(label=_("Your name"), required=True,max_length=255)
    submitter_email = forms.CharField(label=_("Your email address (we'll send you a confirmation email)"), required=True,max_length=255)

    # Captcha field to prevent spam submissions.
    #kontroll = CaptchaField(label=u"Kontrollfråga")

class IdeaVoteForm(forms.Form):
    """Vote for an idea."""
    pass

