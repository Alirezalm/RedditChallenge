from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from comment.models import Comment
from comment.api.v1.serializer import CommentSerializer
from topic.my_permissions import IsAuthorOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def filter_queryset(self, queryset):
        post_id = self.kwargs.get('post_pk')
        return queryset.filter(post__pk=post_id)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthorOrReadOnly, ]
        return super(CommentViewSet, self).get_permissions()
