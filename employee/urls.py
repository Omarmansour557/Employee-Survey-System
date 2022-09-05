from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('signup',views.SignUpViewSet)
router.register('',views.EmployeeViewSet)

urlpatterns = router.urls
