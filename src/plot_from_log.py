import benchmarking.utils
import data.loading
from meb import geometry

n = [1000+3000*i for i in range(10) if 1000+3000*i < 25000]
d = 30
eta = 0.9

func_names = {
        "relaxation_heuristic": "Relaxation-Based Heuristic",
        "shrink": "Shrink Heuristic",
        "shrink_avg": "Shrink (avg) Heuristic",
        "shenmaier": "Shenmaier's Approximation"
    }

filep = r"benchmarks/relaxation_heuristic/uniform_ball_with_outliers/func_n_d30_eta0p9_uniform_ball_with_outliers"
func_name = filep.split("/")[1]

times = benchmarking.utils.get_times_from_log(filepath=r"{}.log".format(filep))
title = benchmarking.utils.get_title(func_name, n, d, eta)
benchmarking.utils.plot_times(
        x_axis=n,
        times=times,
        xlabel="n",
        ylabel="Time",
        title=title,
        plot=True,
        filepath=r"{}.png".format(filep)
    )