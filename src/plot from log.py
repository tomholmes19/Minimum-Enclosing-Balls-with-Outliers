import benchmarking.utils
import data.loading
from meb import geometry

n = 10000
d = [10+10*i for i in range(10)]
eta = 0.9

filep = r"benchmarks/shenmaier/uniform_ball/func_d_n10000_eta0p9_uniform_ball"

times = benchmarking.utils.get_times_from_log(filepath=r"{}.log".format(filep))

benchmarking.utils.plot_times(
        x_axis=d,
        times=times,
        xlabel="n",
        ylabel="Time",
        title="Runtime for Shenmaier's Approximation as a function of d, n={0}, eta={1}".format(n,eta),
        plot=True,
        filepath=r"{}.png".format(filep)
    )