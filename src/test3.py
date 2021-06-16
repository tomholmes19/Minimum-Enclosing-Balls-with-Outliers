import timeit

n = 100000000
my_list = range(n)

full_start = timeit.default_timer()

a = [x for x in my_list if x % 2 == 0]
b = [x for x in my_list if x % 2 == 1]

full_elapsed = timeit.default_timer() - full_start

zeros_start = timeit.default_timer()

a = []
b = []

for x in my_list:
    if x % 2 == 0:
        a.append(x)
    else:
        b.append(x)

zeros_elapsed = timeit.default_timer() - zeros_start

print(full_elapsed, zeros_elapsed)