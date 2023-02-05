from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.datasets.views.dataset import DatasetViewset, TagViewset
from app.datasets.views.file_dataset import DocumentAPIView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("tags", TagViewset)
router.register("", DatasetViewset)


urlpatterns = [
    path("upload/", DocumentAPIView.as_view(), name="documents"),
]
urlpatterns += router.urls
