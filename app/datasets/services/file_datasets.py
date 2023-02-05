from celery.utils.log import get_task_logger
from django.conf import settings
from rest_framework.exceptions import APIException

from app.datasets.models import Dataset

from ..utils.csv import rows_from_a_csv_file

logger = get_task_logger(__name__)


def csv_to_db(file_path: str):
    try:
        Dataset.objects.bulk_create(
            [
                Dataset(user_id=3, text=row[0])
                for row in rows_from_a_csv_file(file_path, skip_first_line=True)
            ],
            batch_size=settings.BATCH_SIZE,
        )
    except Exception as err:
        # TODO:
        raise APIException(f"Error: {err}")
