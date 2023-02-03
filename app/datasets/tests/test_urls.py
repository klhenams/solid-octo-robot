from django.urls import resolve, reverse

from app.datasets.models import Dataset


def test_dataset_detail(unlabeled_data: Dataset):
    assert (
        reverse("app:dataset-detail", kwargs={"pk": unlabeled_data.pk})
        == f"/app/datasets/{unlabeled_data.pk}/"
    )
    assert (
        resolve(f"/app/datasets/{unlabeled_data.pk}/").view_name == "app:dataset-detail"
    )


def test_dataset_list():
    assert reverse("app:dataset-list") == "/app/datasets/"
    assert resolve("/app/datasets/").view_name == "app:dataset-list"
