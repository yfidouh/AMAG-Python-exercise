import os
import pandas as pd

from amag_op.exceptions.file_type_error import FileTypeError, FileDoesNotExistError


def load_file(fname, sheet_name=None):
    """ """
    if not os.path.isfile(fname):
        raise FileDoesNotExistError
    ext = os.path.splitext(fname)[-1].lower()
    # make sure that ext is either .csv or .xlsx or .xls
    if ext == ".csv":
        return pd.read_csv(fname)
    elif ext in [".xlsx", ".xls"]:
        return pd.read_excel(fname, sheet_name=sheet_name)
    else:
        raise FileTypeError(ext)


def save_file(fname, df, sheet_name=None):
    ext = os.path.splitext(fname)[-1].lower()
    # make sure that ext is either .csv or .xlsx or .xls
    if ext == ".csv":
        pd.to_csv(fname, index=False)
    elif ext in [".xlsx", ".xls"]:
        if sheet_name:
            pd.to_excel(fname, sheet_name=sheet_name)
    else:
        raise FileTypeError(ext)
