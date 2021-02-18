from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from comment.models import Comment
from comment.views import CommentListViews, CommentDetailViewSet
from post.views import PostListView, PostDetailList
from topic import views

urlpatterns = [
    path('', views.TopicViewSet),
    path('<str:url_name>/', views.TopicDetailView.as_view()),
    path('<str:url_name>/posts/', PostListView.as_view()),
    path('<str:url_name>/posts/<int:pk>/', PostDetailList.as_view()),
    path('<str:url_name>/posts/<int:pk>/comments/', CommentListViews.as_view()),
    path('<str:url_name>/posts/<int:pk_post>/comments/<int:pk_comment>/', CommentDetailViewSet.as_view())
]

