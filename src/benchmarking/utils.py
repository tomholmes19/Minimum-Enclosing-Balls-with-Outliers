import numpy as np
import matplotlib.pyplot as plt

from data.loading import from_csv

def load_normal(n,d):
    filename = r"src\data\datasets\normal\normal_n{}_d{}.csv".format(n,d)
    data = from_csv(filename=filename)
    return data

def plot_times(x_axis, times, xlabel, ylabel, title, plot, filepath=None):
    """
    Creates a plot for benchmarking

    Input:
        x_axis (array like): x values for points to plot
        times (array like): y values (runtimes) to plot
        xlabel (str): x axis label
        ylabel (str): y axis label
        title (str): title of plot
        plot (bool): if True, display the plot
        filepath (str/None) (optonal): if not None will save the plot to the specified filepath
    
    Return:
        None
    """
    plt.figure()
    plt.plot(x_axis, times, marker="o", linestyle=":", mec="r", mfc="r")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    if filepath is not None:
        plt.savefig(filepath)
    
    if plot:
        plt.show()
    
    return None