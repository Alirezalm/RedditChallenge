from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from post.views import PostListView, PostDetailList
from topic import views

urlpatterns = [
    path('', views.TopicListView.as_view()),
    path('<str:url_name>/', views.TopicDetailView.as_view()),
    path('<str:url_name>/posts/', PostListView.as_view()),
    path('<str:url_name>/posts/<int:pk>/', PostDetailList.as_view())
]

