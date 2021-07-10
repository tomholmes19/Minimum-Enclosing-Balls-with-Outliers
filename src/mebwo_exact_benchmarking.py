import benchmarking.trials, benchmarking.utils
import data.loading

num_trials = 5

data_type = "normal"
normal_filepath = r"datasets/normal.csv"
normal_data = data.loading.from_csv(normal_filepath)
print("Finished loading data")

if True:
    n = [50+ 50*i for i in range(3)]
    eta = 0.9
    d = 8

    file_name = r"{0}/func_n_d{1}_eta{2}_{3}".format(data_type, d, str(eta).replace(".","p"), data_type)
    log_file = r"benchmarks/exact/{0}.log".format(file_name)

    times = benchmarking.trials.run_trials_exact(n, d, eta, num_trials, normal_data, log_file=log_file, data_file=normal_filepath)

    benchmarking.utils.plot_times(
        x_axis=n,
        times=times,
        xlabel="n",
        ylabel="Time",
        title="Running time for MEBwO as a function of n, d={0}, eta={1}".format(d, eta),
        plot=True,
        filepath=r"benchmarks/exact/{0}.png".format(file_name)
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