from rest_framework import generics, permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from app.datasets.serializers.file_upload import FileUploadSerializer
from app.datasets.tasks import csv_to_db_task


class DocumentAPIView(generics.CreateAPIView):
    parser_classes = [FormParser, MultiPartParser]
    serializer_class = FileUploadSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        document = serializer.save()
        csv_to_db_task.delay(document.file.path)
        return Response({"detail": "Accepted for processing"})
