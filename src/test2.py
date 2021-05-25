import data.loading
from meb.ball import Ball

test_data = data.loading.from_csv(r"src\test\normal_test.csv")

ball = Ball().fit(test_data, eps=1e-2)

print(ball)