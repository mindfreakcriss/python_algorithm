import numpy as np

n = 10000

sum = np.sum(4.0 / np.r_[1:n:4,-3:-n:-4])
print(sum)
