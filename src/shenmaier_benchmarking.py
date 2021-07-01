import timeit

from meb.geometry import M_estimate
from meb.ball import MEBwO

from benchmarking.utils import load_normal, plot_times

n_list = [100 + 50*i for i in range(10)]
d_list = [2 + 2*i for i in range(10)]

if False:
    times = []
    d = 4
    eta = 0.9

    for n in n_list:
        data = load_normal(n, d)

        start = timeit.default_timer()
        ball = MEBwO().fit(data=data, method="shenmaier", eta=eta)
        elapsed = timeit.default_timer() - start

        times.append(elapsed)
    
    plot_times(
        x_axis=n_list,
        times=times,
        xlabel="n",
        ylabel="Time",
        title="Shenmaier runtime as a function of n, d={}, eta={}".format(d, eta),
        plot=True
    )

if False:
    times = []
    eta = 0.9
    n = 500

    for d in d_list:
        data = load_normal(n,d)
        
        start = timeit.default_timer()
        ball = MEBwO().fit(data=data, method="shenmaier", eta=eta)
        elapsed = timeit.default_timer() - start

        times.append(elapsed)
    
    plot_times(
        x_axis=d_list,
        times=times,
        xlabel="d",
        ylabel="Time",
        title="Shenmaier runtime as a function of d, n={}, eta={}".format(n, eta),
        plot=True,
        #filepath=r"images\benchmarks\mebwo_runtimes_n{}.png".format(n)
    )

if True:
    times = []

    n = 500
    d = 20
    data = load_normal(n,d)

    eta_list = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]

    for eta in eta_list:
        start = timeit.default_timer()
        ball = MEBwO().fit(data=data, method="shenmaier", eta=eta)
        elapsed = timeit.default_timer() - start

        times.append(elapsed)
    
    plot_times(
        x_axis=eta_list,
        times=times,
        xlabel="eta",
        ylabel="Time",
        title="Shenmaier runtime as a function of eta, n={}, d={}".format(n, d),
        plot=True,
        #filepath=r"images\benchmarks\mebwo_runtimes_eta.png"
    )