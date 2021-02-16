from django.contrib import admin

from topic.models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'author')
    prepopulated_fields = {"name": ("title", )}
