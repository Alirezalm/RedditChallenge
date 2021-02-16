from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from topic import views

urlpatterns = [
    path('', views.TopicListView.as_view()),
    path('<str:url_name>/', views.TopicDetailView.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)