from meb.ball import MEBwO
from data.loading import from_csv

def compare(data, eta):
    """
    Fits an exact and heuristic MEBwO to the data and reports solutions

    Input:
        data (array like): data to fit the MEBwO to
        eta (float): percentage of data to be inside the ball

    Return:
        exact (MEBwO): fit ball object using the exact method
        heuristic (MEBWO): fit ball object using the heuristic
    """
    exact = MEBwO().fit(data, method="exact", eta=eta, calc_pct=True)
    heuristic = MEBwO().fit(data, method="heuristic", eta=eta, calc_pct=True)

    print("=== Exact ===")
    print(exact)

    print("=== Heuristic ===")
    print(heuristic)

    pct_diff = heuristic.radius/exact.radius
    print("\npct. difference: {}%".format(pct_diff))

    return exact, heuristic

data = from_csv(r"src\datasets\normal\normal_n300_d5")
compare(data, eta=0.9)
