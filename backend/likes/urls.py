from rest_framework.routers import SimpleRouter

from .views import LikeViewSet

router = SimpleRouter()
router.register(r"likes", LikeViewSet, basename="likes")

urlpatterns = router.urls
