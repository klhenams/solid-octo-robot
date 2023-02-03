import random

from factory import Sequence, SubFactory, fuzzy, post_generation
from factory.django import DjangoModelFactory

from app.datasets.models import Dataset, Tag
from app.datasets.utils.enumerations import Sentiment
from app.users.tests.factories import UserFactory


class TagFactory(DjangoModelFactory):
    aspect = Sequence(lambda n: "Aspect %d" % n)
    sentiment = random.choice([x[0] for x in Sentiment.choices])

    class Meta:
        model = Tag
        django_get_or_create = ["aspect"]


class DatasetFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    text = fuzzy.FuzzyText(length=350)

    class Meta:
        model = Dataset
        django_get_or_create = ["text"]


class UnlabeledDatasetFactory(DatasetFactory):
    pass


class LabeledDatasetFactory(DatasetFactory):
    @post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for tag in extracted:
                self.tags.add(tag)
