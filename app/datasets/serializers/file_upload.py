from rest_framework import serializers

from app.datasets.models import Document


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
