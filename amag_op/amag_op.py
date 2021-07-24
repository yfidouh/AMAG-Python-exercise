from amag_op.helpers import load_file, save_file
from amag_op.ops import perform_op

import pandas as pd


def parse_row(row):
    return {
        "x": pd.to_numeric(row["x"]),
        "y": pd.to_numeric(row["y"]),
        "op": row["operation"],
    }


def apply_op(x):
    try:
        res = perform_op(**parse_row(x))
        return str(res)
    except Exception as e:
        # maybe log e?
        return str(e)
    return None


def process(fname, sheet_name=None):
    df = load_file(fname, sheet_name)
    cols = ["x", "y", "operation"]
    for col in cols:
        assert col in df.columns, f"missing {col} in columns"
    # for col in cols[:-1]:
    #     df[col] = df[col].apply(pd.to_numeric)

    df["result"] = df.apply(lambda x: apply_op(x), axis=1)

    # maybe check flag to overwrite existing read in file or create new one
    new_fname = ".".join(
        fname.split(".")[:-2] + [fname.split(".")[-2] + "_out." + fname.split(".")[-1]]
    )
    # new_fname = ".".join(fname.split(".")[:-2] + [fname.split(".")[-2] + "_out.csv"])
    save_file(new_fname, df, sheet_name)
    print(f"Saved results to '{new_fname}'")


if __name__ == "__main__":
    pass
