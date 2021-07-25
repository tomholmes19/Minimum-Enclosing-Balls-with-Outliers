import benchmarking.utils
import data.loading
from meb import geometry

n = [1000 + 3000*i for i in range(8)]
d = 30
eta = 0.9

filep = r"benchmarks/shenmaier/uniform_ball/func_n_d30_eta0p9_uniform_ball"

times = benchmarking.utils.get_times_from_log(filepath=r"{}.log".format(filep))

benchmarking.utils.plot_times(
        x_axis=n,
        times=times,
        xlabel="n",
        ylabel="Time",
        title="Runtime for Shenmaier's Approximation as a function of n, d={0}, eta={1}".format(d,eta),
        plot=True,
        filepath=r"{}.png".format(filep)
    )