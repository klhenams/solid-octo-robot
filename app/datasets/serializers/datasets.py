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


class DatasetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Dataset
        fields = [
            "text",
            "tags",
        ]
