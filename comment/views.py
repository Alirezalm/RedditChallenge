from django.http import Http404
from rest_framework import status

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment
from comment.serializer import CommentSerializer
from topic.models import Topic
from topic.my_permissions import IsAuthorOrReadOnly
from topic.serializers import TopicSerializer


class CommentListViews(APIView):

    def get_permissions(self):

        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated,]

        return super().get_permissions()

    def get(self, request, url_name, pk):

        topic = Topic.objects.get(url_name=url_name)
        post = topic.post_set.get(pk = pk)
        comments = post.comment_set.all()

        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

    def post(self, request, url_name, pk):

        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailViewSet(APIView):
    permission_classes = [IsAuthorOrReadOnly, ]

    def get_object(self, url_name, pk_post, pk_comment):
        try:
            topic = Topic.objects.get(url_name=url_name)
            post = topic.post_set.get(pk=pk_post)
            return post.comment_set.get(pk=pk_comment)
        except Topic.DoesNotExist:
            raise Http404

    def get(self, request, url_name, pk_post, pk_comment, format=None):
        comment = self.get_object( url_name, pk_post, pk_comment)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request,url_name, pk_post, pk_comment, format=None):
        comment = self.get_object(url_name, pk_post, pk_comment)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,url_name, pk_post, pk_comment, format=None):
        comment = self.get_object(url_name, pk_post, pk_comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
