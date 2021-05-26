import data.loading, data.generation
from meb.ball import Ball
print("generating data")
test_data = data.generation.normal(0,1,n=10000,dimension=2)
print("finished data")
ball = Ball().fit(test_data, eps=1e-4)

ball.plot(test_data, figsize=8)