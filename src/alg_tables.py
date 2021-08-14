import pandas as pd

import benchmarking.utils

heuristics = ["relaxation_heuristic", "shenmaier", "shrink", "shrink_avg"]
data_types = ["hyperspherical_shell", "normal", "uniform_ball", "uniform_ball_with_outliers"]
params = {
    "n": [1000+3000*i for i in range(10)],
    "d": [10+10*i for i in range(10)],
    "eta": [0.5 + 0.1*i for i in range(5)]
}

fixed_params = {
    "n": "d30",
    "d": "n10000",
    "eta": "n10000_d30"
}

column_headers = [
    "Relaxation-Based Heuristic",
    "Shenmaier's Approximation",
    "Shrink Heuristic",
    "Avg. Point Heuristic"
]

for data_type in data_types:
    for param in params:
        results_dict = {param: params[param], **{heuristic: None for heuristic in heuristics}}
        
        for heuristic in heuristics:
            # construct filename
            filename = "func_{0}_{1}".format(param, fixed_params[param])
            if param != "eta":
                filename += "_eta0p9"
            filename += "_{}".format(data_type)
            
            results = benchmarking.utils.get_r_from_log(r"benchmarks/{0}/{1}/{2}.log".format(heuristic, data_type, filename))
            
            while len(results) < len(params[param]):
                results.append(0)
            results_dict[heuristic] = results
        
        results_df = pd.DataFrame.from_dict(results_dict)
        results_df.columns = [param] + column_headers
        results_df = results_df.round(decimals=4)
        results_df.to_csv(r"tables/{0}/{1}.csv".format(data_type, filename), index=False, sep="&")
            