from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers
from comment.views import CommentViewSet
from comment.models import Comment

from post.views import PostViewSet

from topic import views

router = routers.DefaultRouter()
router.register('topics', viewset=views.TopicViewSet, basename='topics')

post_router = routers.NestedDefaultRouter(router, 'topics', lookup='topic')
post_router.register('posts', PostViewSet, basename='posts')

comment_router = routers.NestedDefaultRouter(post_router, 'posts', lookup='post')
comment_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = router.urls + post_router.urls + comment_router.urls


