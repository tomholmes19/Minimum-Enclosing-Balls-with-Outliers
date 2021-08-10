import benchmarking.trials, benchmarking.utils
import data.loading

heuristic = "dcssh"
n = 1000
d = [50+10*i for i in range(9,10)]
num_trials = 5
num_iter = 100
data_type = "normal"

df = benchmarking.trials.run_trials_improvement_r(heuristic, n, d, num_trials, num_iter, data_type)
print(df)