"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from helpers.health_check_view import health_check

###
# URLs
###
urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Applications
    url(r'^', include('accounts.urls')),

    path('', include('topic.urls')),
    path('', include('post.urls')),
    path('', include('comment.urls')),

    path('api-auth/', include('rest_framework.urls')),
]
