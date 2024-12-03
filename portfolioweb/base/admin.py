from django.contrib import admin

from .models import Project, Skill, Tag,  Endorsement, Comment, Question

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Endorsement)
admin.site.register(Comment)
admin.site.register (Question)
