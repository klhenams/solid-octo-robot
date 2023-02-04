from django.urls import resolve, reverse

from app.datasets.models import Dataset, Tag


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


def test_tag_detail(tag: Tag):
    assert (
        reverse("app:tag-detail", kwargs={"pk": tag.pk})
        == f"/app/datasets/tags/{tag.pk}/"
    )
    assert resolve(f"/app/datasets/tags/{tag.pk}/").view_name == "app:tag-detail"


def test_tag_list():
    assert reverse("app:tag-list") == "/app/datasets/tags/"
    assert resolve("/app/datasets/tags/").view_name == "app:tag-list"
