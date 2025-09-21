import pandas as pd


def get(filepath: str) -> str:
    df = pd.read_csv(filepath)
    return df.columns[0]
