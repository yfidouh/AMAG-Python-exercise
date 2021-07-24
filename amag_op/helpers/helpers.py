import os
import pandas as pd

from amag_op.exceptions.file_type_errors import FileTypeError, FileDoesNotExistError


def load_file(fname, sheet_name=None):
    """ """
    if not os.path.isfile(fname):
        raise FileDoesNotExistError
    ext = os.path.splitext(fname)[-1].lower()
    # make sure that ext is either .csv or .xlsx or .xls
    if ext == ".csv":
        return pd.read_csv(fname)
    elif ext in [".xlsx", ".xls"]:
        if sheet_name:
            return pd.read_excel(fname, sheet_name=sheet_name)
        else:
            return pd.read_excel(fname, sheet_name=0)
    else:
        raise FileTypeError(ext)


def save_file(fname, df, sheet_name=None):
    ext = os.path.splitext(fname)[-1].lower()
    # make sure that ext is either .csv or .xlsx or .xls
    if ext == ".csv":
        df.to_csv(fname, index=False)
    elif ext in [".xlsx", ".xls"]:
        # options = {"strings_to_formulas": False, "strings_to_urls": False}
        # writer = pd.ExcelWriter(fname, engine="xlsxwriter", options=options)
        if sheet_name:
            # df.to_excel(writer, sheet_name, index=False)
            df.to_excel(fname, sheet_name, index=False)
        else:
            df.to_excel(fname, "Sheet 1", index=False)
        # writer.save()
    else:
        raise FileTypeError(ext)
