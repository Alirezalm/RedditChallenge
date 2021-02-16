from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostSerializer
from topic.models import Topic
from topic.my_permissions import IsAuthorOrReadOnly
from topic.serializers import TopicSerializer


class PostListView(APIView):

    def get(self, request, url_name):

        topic = Topic.objects.get(url_name = url_name)
        posts = topic.post_set.all()

        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

    def post(self, request, url_name):

        serializer = TopicSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailList(APIView):
    permission_classes = [IsAuthorOrReadOnly, ]  # user defined permission

    def get_object(self, url_name, pk):
        try:
            topic = Topic.objects.get(url_name=url_name)
            return topic.post_set.get(pk = pk)
        except Topic.DoesNotExist:
            raise Http404

    def get(self, request, pk, url_name, format=None):
        post = self.get_object(url_name, pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, url_name, format=None):
        post = self.get_object(url_name, pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, url_name, format=None):
        post = self.get_object(url_name, pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)