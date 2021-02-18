from django.http import Http404
from rest_framework import status, viewsets

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment
from comment.serializer import CommentSerializer
from topic.models import Topic
from topic.my_permissions import IsAuthorOrReadOnly
from topic.serializers import TopicSerializer


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def filter_queryset(self, queryset):
        post_id = self.kwargs.get('post_pk')
        return queryset.filter(post__pk = post_id)
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthorOrReadOnly, ]
        return super(CommentViewSet, self).get_permissions()
