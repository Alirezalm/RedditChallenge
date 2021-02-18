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