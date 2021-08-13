import pandas as pd
import numpy as np

import benchmarking.trials, benchmarking.utils
from meb.mebwo_algorithms import alg__shrink_avg, alg__shenmaier

np.random.seed(10000)

numbers = range(10)
eta_list = [0.7, 0.75, 0.8, 0.85, 0.9, 0.95]

msg = input("Run for:\n\tShenmaier? 1\n\tShrink Avg? 2\n")
log_file = "benchmarks/"
if msg == "1":
    func = alg__shenmaier
    log_file += "shenmaier"
elif msg == "2":
    func = alg__shrink_avg
    log_file += "shrink_avg"
log_file += "/mnist/mnist_log.log"

df = pd.read_csv(r"datasets/mnist_train.csv", header=None)
print("Finished loading data")
for eta in eta_list:
    for number in numbers:
        benchmarking.trials.mnist_benchmark(df=df, func=func, number=number, eta=eta, log_file=log_file)

benchmarking.utils.notify()