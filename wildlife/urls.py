from rest_framework import routers
from .api import FishViewSet, BugsViewSet, SeaViewSet

router = routers.DefaultRouter()
router.register('api/fish', FishViewSet, 'fish')
router.register('api/bugs', BugsViewSet, 'bugs')
router.register('api/sea', SeaViewSet, 'sea')

urlpatterns = router.urls
