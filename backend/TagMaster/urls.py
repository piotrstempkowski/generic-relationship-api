from rest_framework import routers

from .views import TaggedItemViewSet, BookmarkViewSet, NoteViewSet

router = routers.SimpleRouter()
router.register(r"TaggedItems", TaggedItemViewSet, basename="tagged-items")
router.register(r"bookmark", BookmarkViewSet, basename="bookmark")
router.register("note", NoteViewSet, basename="note")

urlpatterns = router.urls
