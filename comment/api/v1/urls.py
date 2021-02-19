from rest_framework_nested import routers

from comment.api.v1.views import CommentViewSet
from post.api.v1.urls import post_router

comment_router = routers.NestedDefaultRouter(post_router, 'posts', lookup='post')
comment_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = comment_router.urls