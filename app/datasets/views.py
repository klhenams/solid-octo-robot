from django.conf import settings
from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.datasets.utils.enumerations import Sentiment

from .models import Dataset, Tag
from .serializers.datasets import (
    DatasetSerializer,
    TagAspectsOnlySerializer,
    TagSerializer,
)


class DatasetViewset(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def get_queryset(self, *args, **kwargs):
        user = self.request.user.id
        assert isinstance(user, int)

        if f"datasets_{user}" in cache:
            # get results from cache
            return cache.get(f"datasets_{user}")
        else:
            datasets = self.queryset.filter(user_id=user)
            cache.set(f"datasets_{user}", datasets, timeout=settings.CACHE_TTL)
            return datasets

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self, *args, **kwargs):
        if "tags" in cache:
            # get results from cache
            return cache.get("tags")
        else:
            tags = super().get_queryset(*args, **kwargs)
            cache.set("tags", tags, timeout=settings.CACHE_TTL)
            return tags

    @action(detail=False)
    def aspects(self, request):
        return Response(TagAspectsOnlySerializer(self.get_queryset(), many=True).data)

    @action(detail=False)
    def sentiments(self, request):
        return Response(Sentiment.choices)
