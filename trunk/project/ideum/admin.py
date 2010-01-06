# -*- coding: utf-8 -*-
from django.contrib import admin
from ideum.models import *

class TopicAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	search_fields = ['name']

admin.site.register(Idea)
admin.site.register(Citizen)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Pingback)
admin.site.register(Vote)
