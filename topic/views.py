from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from topic.models import Topic
from topic.my_permissions import IsAuthorOrReadOnly
from topic.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated,]


class TopicDetailView(APIView):
    permission_classes = [IsAuthorOrReadOnly,] #user defined permission
    def get_object(self, url_name):
        try:
            return Topic.objects.get(url_name=url_name)
        except Topic.DoesNotExist:
            raise Http404

    def get(self, request, url_name, format=None):
        topic = self.get_object(url_name)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def put(self, request, url_name, format=None):
        topic = self.get_object(url_name)
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, url_name, format=None):
        topic = self.get_object(url_name)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)