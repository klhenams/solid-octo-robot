from django.test import RequestFactory

from app.datasets.models import Dataset, Tag
from app.datasets.views.dataset import DatasetViewset, TagViewset


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


class TestTagViewSet:

    view = TagViewset()

    def test_get_queryset(self, tag: Tag, user, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = user

        self.view.request = request

        assert tag in self.view.get_queryset()

    def test_create_tag(self, user, rf: RequestFactory):
        aspect = "myaspect 1"
        request = rf.post("/fake-url/")
        request.user = user
        request.data = {"aspect": aspect, "sentiment": "POS"}

        self.view.request = request
        self.view.format_kwarg = "json"
        response = self.view.create(request)

        assert response.data["aspect"] == aspect

    def test_update_tag(self, user, tag: Tag, rf: RequestFactory):
        aspect = "myaspect modified"
        request = rf.put("/fake-url/")
        request.user = user
        request.data = {"aspect": aspect, "sentiment": "NEU"}

        self.view.request = request
        self.view.format_kwarg = "json"
        self.view.kwargs = {"pk": tag.pk}
        response = self.view.update(request)

        assert response.data["aspect"] == aspect
