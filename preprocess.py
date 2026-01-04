import pandas as pd

def load_and_preprocess(path):
    df = pd.read_csv(path)

    X = df[["hours_studied", "attendance"]]
    y = df["marks"]

    return X, y
