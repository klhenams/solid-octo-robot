from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.datasets.views.dataset import DatasetViewset, TagViewset

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("tags", TagViewset)
router.register("", DatasetViewset)

urlpatterns = router.urls

urlpatterns += []
