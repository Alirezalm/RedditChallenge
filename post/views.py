from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostSerializer
from topic.models import Topic
from topic.my_permissions import IsAuthorOrReadOnly
from topic.serializers import TopicSerializer


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthorOrReadOnly]

    def filter_queryset(self, queryset):
        topic_url_name = self.kwargs.get('topic_url_name')
        return queryset.filter(topic__url_name=topic_url_name)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthorOrReadOnly,]
        return super(PostViewSet, self).get_permissions()

