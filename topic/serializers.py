from rest_framework import serializers

from topic.models import Topic


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('name', 'title', 'author', 'description', 'created_at')

