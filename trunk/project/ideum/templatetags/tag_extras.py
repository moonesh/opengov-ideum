import urllib, hashlib
from django import template

register = template.Library()

@register.simple_tag
def gravatar(email):
	"""
	Simply gets the Gravatar for the commenter.

	Template Syntax::

		{% gravatar item.user_email %}
	"""

	url = "http://www.gravatar.com/avatar/"
	url += hashlib.md5(email).hexdigest()
	url += "?d=identicon&amp;s=40&amp;d=monsterid"

	return """<img src="%s" alt="" class="gravatar">""" % (url)
