from .helpers import load_file, save_file
from .ops import perform_op


def parse_row(row):
    cols = ["x", "y", "operation"]
    for col in cols:
        assert col in row.cols, f"missing {col} in columns"
    return {
        "x": row["x"],
        "y": row["y"],
        "op": row["operation"],
    }


def apply_op(x):
    try:
        return perform_op(**parse_row(x))
    except Exception as e:
        # maybe log e?
        pass
    return None


def process(fname, sheet_name=None):
    df = load_file(fname, sheet_name)
    df["results"] = df.apply(lambda x: apply_op(x), axis=1)

    # maybe check flag to overwrite existing read in file or create new one
    new_fname = ".".join(fname.split(".")[:-1] + ["_out." + fname.split(".")[-1]])
    save_file(new_fname, df, sheet_name)


if __name__ == "__main__":
    pass
