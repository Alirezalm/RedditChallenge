from rest_framework_nested import routers

from post.api.v1.views import PostViewSet
from topic.api.v1.urls import router

post_router = routers.NestedDefaultRouter(router, 'topics', lookup='topic')
post_router.register('posts', PostViewSet, basename='posts')

urlpatterns = post_router.urls
