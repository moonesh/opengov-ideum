from django.conf.urls.defaults import *

# The start page
ideum_index = url(
    regex  = '^$',
    view   = 'ideum.views.index',
    name   = 'index'
)

# a single idea 
ideum_idea = url(
    regex  = '^(?P<idea_id>\d+)/$',
    view   = 'ideum.views.idea',
    name   = 'idea'
)

#a vote for an idea
ideum_vote = url(
    regex  = '^(?P<idea_id>\d+)/vote/$',
    view   = 'ideum.views.vote',
    name   = 'ideavote'
)

ideum_thankyou = url( 
    regex  = '^thankyou/$',
    view   = 'ideum.views.thankyou',
    name   = 'thankyou'
)


urlpatterns = patterns('', ideum_index, ideum_idea, ideum_thankyou)

