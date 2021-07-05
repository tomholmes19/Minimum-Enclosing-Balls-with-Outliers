from meb.geometry import M_estimate
from benchmarking import utils, trials
from benchmarking.exact_solver import mebwo_exact
from data.loading import from_csv

n_list = [100 + 50*i for i in range(3)]
d_list = [2 + 2*i for i in range(10)]
num_trials = 5

normal = from_csv(r"src\data\datasets\normal.csv")
print("Finished loading data")

if True:
    n = [100 + 50*i for i in range(3)]
    eta = 0.9
    d = 8

    times = trials.run_trials_exact(n, d, eta, num_trials, normal)

    utils.plot_times(
        x_axis=n_list,
        times=times,
        xlabel="n",
        ylabel="Time",
        title="Running time for MEBwO as a function of n, d={}, eta={}".format(d, eta),
        plot=True,
        #filepath=r"images\benchmarks\mebwo_runtimes_d{}.png".format(d)
    )


if False:
    times = []
    eta = 0.9
    n = 300

    for d in d_list:
        data = utils.load_normal(n,d)
        M = M_estimate(data)
        times.append(mebwo_exact(data, eta, M))
    
    utils.plot_times(
        x_axis=d_list,
        times=times,
        xlabel="d",
        ylabel="Time",
        title="Running time for MEBwO as a function of d, n={}, eta={}".format(n, eta),
        plot=True,
        filepath=r"images\benchmarks\mebwo_runtimes_n{}.png".format(n)
    )

if False:
    times = []

    n = 500
    d = 12
    data = utils.load_normal(n,d)
    M = M_estimate(data)

    eta_list = [0.75, 0.8, 0.85, 0.9, 0.95, 1]

    for eta in eta_list:
        times.append(mebwo_exact(data, eta, M))
    
    utils.plot_times(
        x_axis=eta_list,
        times=times,
        xlabel="eta",
        ylabel="Time",
        title="Running time for MEBwO as a function of eta, n={}, d={}".format(n, d),
        plot=True,
        filepath=r"images\benchmarks\mebwo_runtimes_eta.png"
    )

if False:
    times = []

    n = 200
    d = 7
    eta = 0.9

    data = utils.load_normal(n,d)

    M_UB = M_estimate(data)
    M_list = [M_UB*m for m in range(1,11)]

    for M in M_list:
        times.append(mebwo_exact(data, eta, M))
    
    utils.plot_times(
        x_axis=M_list,
        times=times,
        xlabel="M",
        ylabel="Time",
        title="Running time for MEBwO as a function of M, n={}, d={}, eta={}".format(n, d, eta),
        plot=True,
        filepath=r"images\benchmarks\mebwo_runtimes_M.png"
    )