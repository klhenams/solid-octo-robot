from django.core.cache import cache
from rest_framework import serializers

from app.datasets.models import Dataset, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "aspect",
            "sentiment",
        ]


class TagAspectsOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["aspect"]


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = [
            "text",
            "tags",
        ]


class NestedDatasetSerializer(DatasetSerializer):
    tags = TagSerializer(many=True, required=False)

    def create(self, validated_data):

        if "tags" in validated_data.keys():
            tags = TagSerializer(many=True).create(validated_data.pop("tags"))
            dataset = super().create(validated_data=validated_data)
            dataset.tags.add(*tags)
        else:
            dataset = super().create(validated_data=validated_data)

        # We explicitly deleting cache for tags and datasets
        # because there maybe new additions.
        dataset_key = f"datasets_{dataset.user.id}"
        cache.delete(["tags", dataset_key])
        return dataset
