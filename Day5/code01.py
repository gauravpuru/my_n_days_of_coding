#playing with *args and **kwargs
import numpy as np
def add_func(*args):
    return np.sum(args)

print(add_func(4,5,6))