from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('employee',views.EmployeeViewSet)

urlpatterns = router.urls
