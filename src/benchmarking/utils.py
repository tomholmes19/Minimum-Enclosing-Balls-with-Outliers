import time
import logging
import subprocess
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

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

def progress_report(x, param_name, i) -> None:
    """
    Prints the current step in the benchmarking process

    Input:
        x (float): the parameter being benchmarked (i.e. number of points/dimension)
        param_name (str): name of the parameter being benchmarked
        i (int): current trial of x
    
    Return:
        None
    """
    bar = "===================="
    print(bar)
    print("PROGRESS:")
    print("\t{0}:\t{1}".format(param_name, x))
    print("\tTrial:\t{}".format(i+1))
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
        "Finished trial {0}/{1}, ".format(trial_number+1, num_trials) +
        "elapsed={}, ".format(elapsed) +
        "n={0}, d={1}, eta={2}, M={3}, ".format(n,d,eta,M) +
        "r={0}, c={1}, ".format(r,c) +
        "data={0}, rows={1}, columns={2}".format(data_filepath, rows, columns)
    )
    logging.info(msg)
    print("Recorded log to {}".format(filepath))
    return None

def get_times_from_log(filepath, calc_avg=True) -> list:
    """
    Scans the given log file and returns a list of the runtimes

    Input:
        filepath (str): filepath of the log file to be scanned
        calc_avg (bool): if False then returns list containing lists for each trial, if True then returns list of average times
    
    Output:
        times (list): list of runtimes
    """
    times = []
    trial_times = []

    with open(filepath, "r") as f:
        #num_trials = f.readline().split(sep=", ")[0].split("/")[1]

        for line in f: # iterate over each line
            line_split = line.split(sep=", ") # split into elements of a list
            first_part = line_split[0]

            if "Finished trial" in first_part: # indicator that this is a log written by benchmark_logger
                num_trials = first_part.split("/")[1]
                time = float(line_split[1].split("=")[1]) # line_split[1] will be "elapsed=<time>"
                trial_times.append(time)

                trial_num = first_part.split()[-1].split("/")[0] # which trial number we are on
                if trial_num == num_trials: # i.e. if we are on trial 5/5
                    times.append(trial_times)
                    trial_times = [] # reset

    if calc_avg:
        times = calc_avg_times(times)
    
    return times

def timeout(log_Path, time_limit=20):
    print("Received no input within {} seconds. Continuing.".format(time_limit))
    log_Path.unlink()
    return None

def check_log(log_file, time_limit=20) -> None:
    """
    Checks if the given log_file already exists, and if so asks the user if it should continue.

    Input:
        log_file (str): file path for log file
        time_limit (float): time limit for user prompt
    
    Return:
        None
    """
    if log_file is not None:
        log_Path = Path(log_file)
        if log_Path.exists():
            try:
                print("Log file {0} already exists. Overwriting in {1}s. Press Ctrl+C to abort.".format(log_file, time_limit))
                time.sleep(time_limit)
            except KeyboardInterrupt:
                exit("Aborting.")
    
    return None

def notify() -> None:
    """
    Sends a notification to the notify-run channel in notify.sh
    """
    subprocess.call(["sh", "src/notify.sh"])
    return None

def format_eta(eta) -> str:
    """
    Formats eta for use in a file name, e.g. 0.95 -> 0p95

    Input:
        eta (float): eta value
    
    Return:
        eta_str (str): eta as a string
    """
    eta_str = str(eta).replace(".","p")
    return eta_str