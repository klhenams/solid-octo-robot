from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.datasets.views import DatasetViewset

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("", DatasetViewset)

urlpatterns = router.urls

urlpatterns += []
