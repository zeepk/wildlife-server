from rest_framework import routers
from .api import FishViewSet, BugsViewSet, SeaViewSet, CaughtViewSet
from .views import nice

router = routers.DefaultRouter()
router.register('api/fish', FishViewSet, 'fish')
router.register('api/bugs', BugsViewSet, 'bugs')
router.register('api/sea', SeaViewSet, 'sea')
router.register('api/caught', CaughtViewSet, 'caught')

urlpatterns = router.urls
