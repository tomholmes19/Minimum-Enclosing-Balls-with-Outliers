import benchmarking.utils
import data.loading
from meb import geometry

normal_filepath = r"datasets/normal.csv"
normal_data = data.loading.from_csv(normal_filepath)

n = 300
d = 10
eta = 0.9

rows = range(n)
columns = range(d)

exp_data = data.loading.subset_data(normal_data, rows, columns)

M_UB = geometry.M_estimate(exp_data)
M_list = [M_UB*i for i in range(1,11)][:8]


times = benchmarking.utils.get_times_from_log(filepath=r"benchmarks/exact/normal/func_M_n300_d10_eta0p9_normal.log")

benchmarking.utils.plot_times(
        x_axis=M_list,
        times=times,
        xlabel="M",
        ylabel="Time",
        title="Running time for MEBwO as a function of M, n={}, d={}, eta={}".format(n, d, eta),
        plot=True,
        #filepath=r"images\benchmarks\mebwo_runtimes_M.png"
    )