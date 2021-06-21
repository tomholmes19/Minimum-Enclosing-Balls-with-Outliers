import pandas as pd
from meb.ball import MEB, MEBwO
import timeit

df = pd.read_csv("src\datasets\mnist\mnist_train.csv", header=None)

zeros = df[df[0] == 0]
zeros_no_labels = zeros.drop(labels=0, axis=1)

data = zeros_no_labels.to_numpy()

print("Fit ball")
start = timeit.default_timer()
ball = MEBwO().fit(data=data, method="heuristic", eta=0.9, eps=1e-2)
elapsed = timeit.default_timer() - start

print("Elapsed:\t{}\n".format(elapsed))

ones = df[df[0] == 1]
ones_no_labels = ones.drop(labels=0, axis=1)
ones_data = ones_no_labels.to_numpy()

n = len(ones_data)
inside = 0
for x in ones_data:
    if ball.contains(x):
        inside += 1

print(inside/n)