from rest_framework.routers import SimpleRouter

from .views import BlogViewSet

router = SimpleRouter()
router.register(r"blog", BlogViewSet, basename="blog")

urlpatterns = router.urls
