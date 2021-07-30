import numpy as np
import timeit

from meb.meb_algorithms import alg__socp_heuristic

from . import utils
import meb
import data

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
            c, r, _, trials[i] = meb.gurobi_solvers.mebwo(trial_data, eta_, M, log_file=log_file)
            
            if log_file is not None:
                utils.benchmark_logger(filepath=log_file, elapsed=trials[i], n=n_, d=d_, eta=eta_, M=M, r=r, c=c, trial_number=i, num_trials=num_trials, data_filepath=data_file, rows=rows, columns=columns)
        
        times.append(trials)
    
    avg_times = utils.calc_avg_times(times)

    return avg_times

def run_trials_alg(func, n, d, eta, num_trials, data_type, log_file=None, **kwargs):
    params = {"n": n, "d": d, "eta": eta}

    trial_param, trial_param_vals = utils.find_trial_param(params)

    utils.check_log(log_file)

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

            # load data
            filename = r"datasets/{0}/{1}_n{2}_d{3}".format(data_type, data_type, n_, d_)
            if data_type == "uniform_ball_with_outliers":
                filename += r"_eta{}".format(utils.format_eta(eta_))
            filename += r"_{}.csv".format(i)
            data_ = data.loading.from_csv(filename)

            # only need to calculate M when data is normal
            if data_type == "normal" and func == meb.mebwo_algorithms.alg__relaxation_heuristic:
                _, r, _ = alg__socp_heuristic(data_, eps=1e-4)
                kwargs["M"] = 2*r

            start = timeit.default_timer()
            c, r, _ = func(data_, eta_, **kwargs)
            elapsed = timeit.default_timer() - start

            trials[i] = elapsed

            if log_file is not None:
                if func in [meb.mebwo_algorithms.alg__shrink, meb.mebwo_algorithms.alg__shenmaier]:
                    kwargs["M"] = None

                utils.benchmark_logger(filepath=log_file, elapsed=trials[i], n=n_, d=d_, eta=eta_, M=kwargs["M"], r=r, c=c, trial_number=i, num_trials=num_trials, data_filepath=filename)

        times.append(trials)
    
    avg_times = utils.calc_avg_times(times)

    return avg_times
