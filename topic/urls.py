from django.urls import include, path

urlpatterns = [
    path('', include('topic.api.v1.urls')),

]