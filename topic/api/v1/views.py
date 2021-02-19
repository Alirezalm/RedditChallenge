from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from topic.models import Topic
from topic.api.v1.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'url_name'
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated,]
        return super(TopicViewSet, self).get_permissions()
