from rest_framework_nested import routers
from topic.api.v1 import views

router = routers.DefaultRouter()
router.register('topics', viewset=views.TopicViewSet, basename='topics')

urlpatterns = router.urls


