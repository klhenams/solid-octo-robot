from rest_framework import viewsets

from .models import Dataset
from .serializers.datasets import DatasetSerializer


class DatasetViewset(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(user_id=self.request.user.id)
