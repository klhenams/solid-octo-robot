from django.test import RequestFactory

from app.datasets.models import Dataset
from app.datasets.views import DatasetViewset


class TestDatasetViewSet:
    view = DatasetViewset()

    def test_get_unlabeled_data_queryset(
        self, unlabeled_data: Dataset, rf: RequestFactory
    ):
        request = rf.get("/fake-url/")
        request.user = unlabeled_data.user

        self.view.request = request

        assert unlabeled_data in self.view.get_queryset()

    def test_create_unlabeled_data(self, user, rf: RequestFactory):
        dataset = "The quick brown fox jumps over the lazy dog"
        request = rf.post("/fake-url/")
        request.user = user
        request.data = {"text": dataset}

        self.view.request = request
        self.view.format_kwarg = "json"
        response = self.view.create(request)

        assert response.data["text"] == dataset

    def test_get_labeled_data_queryset(self, labeled_data: Dataset, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = labeled_data.user

        self.view.request = request

        assert labeled_data in self.view.get_queryset()

    def test_create_labeled_data(self, user, rf: RequestFactory):
        dataset = "The quick brown fox jumps over the lazy dog"
        tags = [{"aspect": "Myaspect1", "sentiment": "NEU"}]
        request = rf.post("/fake-url/")
        request.user = user
        request.data = {"text": dataset, "tags": tags}

        self.view.request = request
        self.view.format_kwarg = "json"
        response = self.view.create(request)

        assert response.data["tags"][0]["aspect"] == tags[0]["aspect"]
