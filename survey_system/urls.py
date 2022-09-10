from email.mime import base
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('',views.SurveyViewSet, basename='survey-list')
router.register('aa',views.DemoViewSet, basename='hazem')
urlpatterns = router.urls

