from meb.geometry import M_estimate
from . import utils, exact_solver
import meb
import data

def run_trials_exact(n, d, eta, num_trials, data_):
    """
    
    """
    trial_param = None
    params = {"n": n, "d": d, "eta": eta}
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
        params[trial_param] = x

        n_ = params["n"]
        d_ = params["d"]
        eta_ = params["eta"]

        trials = [0]*num_trials

        for i in range(num_trials):
            utils.progress_report(n_,i)

            trial_data = data.loading.subset_data(data_, range(n_), range(d_))
            M = meb.geometry.M_estimate(trial_data)
            trials[i] = exact_solver.mebwo_exact(trial_data, eta_, M)
        
        times.append(trials)
    
    avg_times = utils.calc_avg_times(times)

    return avg_times
        