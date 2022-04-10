from testapp.views import Employee_detail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'empl', Employee_detail, basename='emp')
urlpatterns = router.urls

