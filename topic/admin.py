from django.contrib import admin

from topic.models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'author', 'url_name')
    prepopulated_fields = {"url_name": ("title", )}
