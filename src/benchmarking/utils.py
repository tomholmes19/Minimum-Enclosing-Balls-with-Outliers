import logging
import numpy as np
import matplotlib.pyplot as plt

def calc_avg_times(avg_times) -> list:
    """
    Takes a list of list in the form [ [*], [*], ...] and returns a list with the average of each sublist

    Input:
        avg_times (list of list of floats): list of lists of times to find average times for

    Return:
        times (list of floats): list of average times
    """
    times = []
    for lst in avg_times:
        times.append(np.mean(lst))
    
    return times

def plot_times(x_axis, times, xlabel, ylabel, title, plot, filepath=None) -> None:
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

def progress_report(x, i) -> None:
    """
    Prints the current step in the benchmarking process

    Input:
        x (float): the parameter being benchmarked (i.e. number of points/dimension)
        i (int): current trial of x
    
    Return:
        None
    """
    bar = "===================="
    print(bar)
    print("PROGRESS:")
    print("\tParam:\t{}".format(x))
    print("\tTrial:\t{}".format(i))
    print(bar)

    return None

def benchmark_logger(filepath, elapsed, n, d, eta, M, r, c, xi, trial_number, num_trials, data_filepath, rows, columns):
    """
    After a trial has been completed, logs details to the specified file

    Input:
        filepath (str): filepath of the log file to be written to
        elapsed (float): elapsed runtime of trial
        n (int): number of rows used in data
        d (int): dimension of data
        eta (float): proportion of points covered by the MEBwO
        M (float): big M parameter for solving exact model
        r (float): solution for radius
        c (list): solution for center
        xi (list): solutions for binary variables
        trial_number (int): current trial in experiment
        num_trials (int): total number of trials in experiment
        data_filepath (str): filepath of data used
        rows (list): rows in data that have been used
        columns (list): columns in data that have been used
    
    Return:
        None
    """
    logging.basicConfig(filename=filepath, encoding='utf-8', format='%(asctime)s %(message)s', level=logging.INFO)
    
    msg = (
        "Finished trial {0}/{1}, ".format(trial_number, num_trials) +
        "elapsed={}, ".format(elapsed) +
        "n={0}, d={1}, eta={2}, M={3}, ".format(n,d,eta,M) +
        "r={0}, c={1}, ".format(r,c) +
        "data={0}, rows={1}, columns={2} ".format(data_filepath, rows, columns)
    )
    logging.info(msg)
    print("Recorded log to {}".format(filepath))
    return None