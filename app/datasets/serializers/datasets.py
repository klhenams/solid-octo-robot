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
            # TODO: unset cache
            return dataset
        return super().create(validated_data=validated_data)
