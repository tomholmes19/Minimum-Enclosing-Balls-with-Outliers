import benchmarking.utils

n = [50+ 50*i for i in range(10)]
eta = 0.9
d = 8
times = benchmarking.utils.get_times_from_log(filepath=r"src/test/test_log.log")

benchmarking.utils.plot_times(
        x_axis=n,
        times=times,
        xlabel="n",
        ylabel="Time",
        title="Running time for MEBwO as a function of n, d={}, eta={}".format(d, eta),
        plot=True,
        #filepath=r"images/benchmarks/mebwo_runtimes_d{}.png".format(d)
    )