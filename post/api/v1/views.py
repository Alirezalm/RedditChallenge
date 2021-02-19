from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from post.models import Post
from post.api.v1.serializers import PostSerializer
from topic.my_permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def filter_queryset(self, queryset):
        topic_url_name = self.kwargs.get('topic_url_name')
        return queryset.filter(topic__url_name=topic_url_name)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthorOrReadOnly,]
        return super(PostViewSet, self).get_permissions()

