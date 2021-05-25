import numpy as np
import pandas as pd

def to_csv(data, filename) -> None:
    df = pd.DataFrame(data)
    df.to_csv(r"{}".format(filename))
    return None

def from_csv(filename) -> np.array:
    df = pd.read_csv(r"{}".format(filename))
    out = df.to_numpy()
    return out