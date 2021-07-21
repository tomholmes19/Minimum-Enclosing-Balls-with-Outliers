import numpy as np

from . import utils
import meb.geometry, meb.gurobi_solvers
import data

#TODO: aaaaaaa
def run_trials_exact(n, d, eta, num_trials, data_, log_file=None, data_file=None):
    """
    Runs trials for the exact solver for MEBwO and returns averaged runtimes
    One of n, d, eta should be a list for benchmarking on that parameter

    Input:
        n (int): number of data points (rows)
        d (int): dimension of data (columns)
        eta (float): proportion of data covered by MEBwO
        num_trials (int): number of trials to run for each experiment (for averaging)
        data_ (np.array): data set
        log_file (str) (default None): file path for log file (if None, no logging)
        data_file (str): file path for original data (for logging)
    
    Return:
        avg_times (list of floats): average runtime for each experiment
    """
    # store variables by references in params dictionary
    params = {"n": n, "d": d, "eta": eta}
    
    trial_param, trial_param_vals = utils.find_trial_param

    utils.check_log(log_file)

    data_shape = data_.shape
    num_rows = data_shape[0]
    num_columns = data_shape[1]

    times = []

    for x in trial_param_vals:
        # update trial parameter in vars dictionary
        params[trial_param] = x

        # update all parameters (will be unchanged except for the trial parameter)
        n_ = params["n"]
        d_ = params["d"]
        eta_ = params["eta"]

        # elapsed time for each trial
        trials = [0]*num_trials

        for i in range(num_trials):
            utils.progress_report(x, trial_param, i)

            # get combination of rows/columns
            rows = np.random.choice(num_rows, size=n_, replace=False)
            columns = np.random.choice(num_columns, size=d_, replace=False)

            # load subset of data and calculate M
            trial_data = data.loading.subset_data(data_, rows, columns)
            M = meb.geometry.M_estimate(trial_data)

            # solve model and store variables
            c, r, xi, trials[i] = meb.gurobi_solvers.mebwo(trial_data, eta_, M, log_file=log_file)
            
            if log_file is not None:
                utils.benchmark_logger(filepath=log_file, elapsed=trials[i], n=n_, d=d_, eta=eta_, M=M, r=r, c=c, xi=xi, trial_number=i, num_trials=num_trials, data_filepath=data_file, rows=rows, columns=columns)
        
        times.append(trials)
    
    avg_times = utils.calc_avg_times(times)

    return avg_times

def run_trials_alg(method, n, d, eta, num_trials, data_path, log_file=None, **kwargs):
    params = {"n": n, "d": d, "eta": eta}

    trial_param, trial_param_vals = utils.find_trial_param

    utils.check_log(log_file)