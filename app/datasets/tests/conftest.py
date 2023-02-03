import pytest

from app.datasets.models import Dataset, Tag
from app.datasets.tests.factories import (
    LabeledDatasetFactory,
    TagFactory,
    UnlabeledDatasetFactory,
)


@pytest.fixture
def tag(db) -> Tag:
    return TagFactory()


@pytest.fixture
def tag1(db) -> Tag:
    return TagFactory(1)


@pytest.fixture
def unlabeled_data(db) -> Dataset:
    return UnlabeledDatasetFactory()


@pytest.fixture
def labeled_data(db, tag) -> Dataset:
    return LabeledDatasetFactory.create(tags=(tag,))


@pytest.fixture
def labeled_data_with_2tags(db, tag, tag1) -> Dataset:
    return LabeledDatasetFactory.create(tags=(tag, tag1))
