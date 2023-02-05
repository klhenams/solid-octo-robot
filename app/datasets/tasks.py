from celery import shared_task

from app.datasets.services.file_datasets import csv_to_db


# @shared_task(ignore_result=True, store_errors_even_if_ignored=True)
@shared_task
def csv_to_db_task(user: int, file_path: str):
    try:
        csv_to_db(user, file_path)
    except Exception as err:  # noqa F841
        pass
