import csv


def rows_from_a_csv_file(filename, skip_first_line=False, dialect="excel", **fmtparams):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, dialect, **fmtparams)
        if skip_first_line:
            next(reader, None)
        yield from reader
