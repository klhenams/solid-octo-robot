import csv

from django.http import HttpResponse


def rows_from_a_csv_file(filename, skip_first_line=False, dialect="excel", **fmtparams):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, dialect, **fmtparams)
        if skip_first_line:
            next(reader, None)
        yield from reader


def get_csv_operators(filename):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename=f"{filename}.csv"'},
    )
    return response, csv.writer(response)
