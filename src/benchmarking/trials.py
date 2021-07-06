from . import utils
import meb.geometry, meb.gurobi_solvers
import data

def run_trials_exact(n, d, eta, num_trials, data_, log_file=None, data_file=None):
    """
    
    """
    # store variables by references in params dictionary
    params = {"n": n, "d": d, "eta": eta}
    trial_param = None
    # find which parameter is the list
    for param, val in params.items():
        if type(val) == list:
            trial_param = param
            trial_param_vals = val.copy()
            break
    
    if trial_param is None:
        raise TypeError("No list of parameters was found")

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
            utils.progress_report(n_,i)

            #TODO: make these random
            rows = range(n_)
            columns = range(d_)

            # load subset of data and calculate M
            trial_data = data.loading.subset_data(data_, rows, columns)
            M = meb.geometry.M_estimate(trial_data)

            # solve model and store variables
            c, r, xi, trials[i] = meb.gurobi_solvers.mebwo_exact(trial_data, eta_, M)
            
            if log_file is not None:
                utils.benchmark_logger(filepath=log_file, elapsed=trials[i], n=n_, d=d_, eta=eta_, M=M, r=r, c=c, xi=xi, trial_number=i, num_trials=num_trials, data_filepath=data_file, rows=rows, columns=columns)
        
        times.append(trials)
    
    avg_times = utils.calc_avg_times(times)

    return avg_times
        