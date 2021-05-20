import numpy as np
import xpress as xp

d = 3 # dimension
n = 1000 # number of data points

def gen_data(n,d):
    data = [0]*n
    for i in range(n):
        data[i] = np.array([np.random.normal(0,1) for _ in range(d)])
    return data

data = gen_data(n,d)

m = xp.problem(name="min enclosing ball") # problem object

r = xp.var(name="radius") # radius dv
c = np.array([xp.var(name="c_{}".format(i), lb=-xp.infinity) for i in range(d)]) # center dv's

m.addVariable(r, c)
m.setObjective(r)

m.addConstraint(xp.sqrt(xp.Dot(c-data[i], c-data[i])) - r <= 0 for i in range(n)) # norm constraint

m.solve()

print("Solution:\n\tr = {}\n\tc = {}".format(m.getSolution(r), m.getSolution(c)))