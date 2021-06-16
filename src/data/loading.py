import numpy as np
import pandas as pd

def to_csv(data, filename) -> None:
    """
    Converts a dataset from np.array to pd.DataFrame then writes to a .csv file

    Input:
        data (np.array): data to be written to csv
        filename (str): filename/path of csv to be written to
    
    Return:
        None
    """
    df = pd.DataFrame(data)
    df.to_csv(r"{}".format(filename), header=False, index=False)
    return None

def from_csv(filename) -> np.array:
    """
    Reads a dataset in .csv format and converts to a np.array

    Input:
        filename (str): filename/path of csv to be read
    
    Return:
        out (np.array): data in np.array format
    """
    df = pd.read_csv(r"{}".format(filename), header=None)
    out = df.to_numpy()
    return out