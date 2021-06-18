import timeit
import matplotlib.pyplot as plt

from data.loading import from_csv
from meb.ball import MEBwO

n_list = [100, 500, 1000, 5000, 10000]
d_list = [5, 10, 15, 20, 50, 100]

def load_normal(n,d):
    filename = r"src\datasets\normal\normal_n{}_d{}".format(n,d)
    data = from_csv(filename=filename)
    return data

if False:
    times = []
    eta = 0.9
    d = 10

    for n in n_list:
        data = load_normal(n,d)

        start = timeit.default_timer()
        ball = MEBwO().fit(data=data, method="heuristic", eta=eta)
        elapsed = timeit.default_timer() - start

        times.append(elapsed)

    plt.plot(n_list, times, marker="o", linestyle=":", mec="r", mfc="r")
    plt.xlabel("n")
    plt.ylabel("Time")
    plt.title("Running time for MEBwO heuristic as a function of n, d={}, eta={}".format(d, eta))
    plt.savefig("images\mebwo_heuristic_runtimes_d{}.png".format(d))
    plt.show()
    

if False:
    times = []
    eta = 0.9
    n = 1000
    for d in d_list:
        data = load_normal(n,d)

        start = timeit.default_timer()
        ball = MEBwO().fit(data=data, method="heuristic", eta=0.9)
        elapsed = timeit.default_timer() - start

        times.append(elapsed)
    
    plt.plot(d_list, times, marker="o", linestyle=":", mec="r", mfc="r")
    plt.xlabel("d")
    plt.ylabel("Time")
    plt.title("Running time for MEBwO heuristic as a function of d, n={}, eta={}".format(n, eta))
    plt.savefig("images\mebwo_heuristic_runtimes_n{}.png".format(n))
    plt.show()

if False:
    times = []

    n = 5000
    d = 10
    data = load_normal(n,d)

    eta_list = [0.75, 0.8, 0.85, 0.9, 0.95, 1]

    for eta in eta_list:
        start = timeit.default_timer()
        ball = MEBwO().fit(data=data, method="heuristic", eta=eta)
        elapsed = timeit.default_timer() - start

        times.append(elapsed)
    
    plt.plot(eta_list, times, marker="o", linestyle=":", mec="r", mfc="r")
    plt.xlabel("eta")
    plt.ylabel("Time")
    plt.title("Running time for MEBwO heuristic as a function of eta, n={}, d={}".format(n, d))
    plt.savefig("images\mebwo_heuristic_runtimes_eta.png")
    plt.show()

if True:
    times = []

    n = 5000
    d = 10
    eta = 0.9

    data = load_normal(n,d)

    M_list = [5, 7.5, 10, 15, 20, 30, 40, 60, 80, 100]

    for M in M_list:
        start = timeit.default_timer()
        ball = MEBwO().fit(data=data, method="heuristic", eta=eta, M=M)
        elapsed = timeit.default_timer() - start

        times.append(elapsed)
    
    plt.plot(M_list, times, marker="o", linestyle=":", mec="r", mfc="r")
    plt.xlabel("M")
    plt.ylabel("Time")
    plt.title("Running time for MEBwO heuristic as a function of M, n={}, d={}, eta=eta".format(n, d, eta))
    plt.savefig("images\mebwo_heuristic_runtimes_M.png")
    plt.show()