import benchmarking.trials, benchmarking.utils
import data.loading

heuristic = "dcmeb"
n = [1000, 4000]
d = 30
num_trials = 5
num_iter = 10
data_type = "normal"

df = benchmarking.trials.run_trials_improvement(heuristic, n, d, num_trials, num_iter, data_type)
print(df)