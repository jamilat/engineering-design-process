import csv
import sys
from pathlib import Path
import pandas as pd

DEFAULT_PATH = "engr90051-IDE(HNW table).csv"

def load(path: str | Path) -> pd.DataFrame:
    """Load the CSV into a DataFrame."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {path}")
    return pd.read_csv(path)

def summarise(df: pd.DataFrame) -> None:
    """Print shape, columns, dtypes, head, and a few useful breakdowns."""
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns\n")

    print("Columns and dtypes:")
    for col, dtype in df.dtypes.items():
        print(f"  - {col}: {dtype}")
    print()

    print("First 5 rows:")
    print(df.head().to_string(index=False))
    print()

    if "Quadrant" in df.columns:
        print("Rows per Quadrant:")
        print(df["Quadrant"].value_counts().to_string())
        print()

    if "Score" in df.columns:
        print("Score summary:")
        print(df["Score"].describe().to_string())
        print()

def read(args):
    path = args[1] if len(sys.argv) > 1 else DEFAULT_PATH
    df = load(path)
    summarise(df)


if __name__ == '__main__':
    args = sys.argv
    read(args) #