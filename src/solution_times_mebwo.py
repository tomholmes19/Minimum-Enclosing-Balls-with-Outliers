import timeit
import matplotlib.pyplot as plt

from data.loading import from_csv
from meb.ball import MEBwO

#TODO: turn these into functions

n_list = [100, 200, 300, 400]
d_list = [3, 7, 11, 15]

def load_normal(n,d):
    filename = r"src\datasets\normal\normal_n{}_d{}.csv".format(n,d)
    data = from_csv(filename=filename)
    return data

if False:
    times = []
    eta = 0.9
    d = 3

    for n in n_list[:-1]:
        data = load_normal(n,d)
        start = timeit.default_timer()
        ball = MEBwO().fit(data=data, method="exact", eta=eta)
        elapsed = timeit.default_timer() - start

        times.append(elapsed)
    
    plt.plot(n_list, times, marker="o", linestyle=":", mec="r", mfc="r")
    plt.xlabel("n")
    plt.ylabel("Time")
    plt.title("Running time for MEBwO as a function of n, d={}, eta={}".format(d, eta))
    plt.savefig("images\mebwo_runtimes_d{}.png".format(d))
    #plt.show()

if False:
    times = []
    eta = 0.9
    n = 300

    for d in d_list:
        data = load_normal(n,d)

        start = timeit.default_timer()
        ball = MEBwO().fit(data=data, method="exact", eta=eta)
        elapsed = timeit.default_timer()

        times.append(elapsed)
    
    plt.plot(d_list, times, marker="o", linestyle=":", mec="r", mfc="r")
    plt.xlabel("d")
    plt.ylabel("Time")
    plt.title("Running time for MEBwO as a function of d, n={}, eta={}".format(n, eta))
    plt.savefig("images\mebwo_runtimes_n{}.png".format(n))
    #plt.show()

if False:
    times = []

    n = 300
    d = 3
    data = load_normal(n,d)

    eta_list = [0.8, 0.85, 0.9, 0.95, 1]

    for eta in eta_list:
        start = timeit.default_timer()
        ball = MEBwO().fit(data=data, method="exact", eta=eta)
        elapsed = timeit.default_timer() - start

        times.append(elapsed)
    
    plt.plot(eta_list, times, marker="o", linestyle=":", mec="r", mfc="r")
    plt.xlabel("eta")
    plt.ylabel("Time")
    plt.title("Running time for MEBwO as a function of eta, n={}, d={}".format(n, d))
    plt.savefig("images\mebwo_runtimes_eta.png")
    #plt.show()

if True:
    times = []

    n = 300
    d = 3
    eta = 0.9

    data = load_normal(n,d)

    M_list = [10, 20, 30, 40, 50]

    for M in M_list:
        start = timeit.default_timer()
        ball = MEBwO().fit(data=data, method="exact", eta=eta, M=M)
        elapsed = timeit.default_timer() - start

        times.append(elapsed)
    
    plt.plot(M_list, times, marker="o", linestyle=":", mec="r", mfc="r")
    plt.xlabel("M")
    plt.ylabel("Time")
    plt.title("Running time for MEBwO as a function of M, n={}, d={}, eta=eta".format(n, d, eta))
    plt.savefig("images\mebwo_runtimes_M.png")
    #plt.show()