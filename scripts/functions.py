from functools import partial

def division (y, x):
    return x/y

divide_by_two = partial(division,8)

print(divide_by_two(4))
